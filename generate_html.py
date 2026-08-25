import os
import re
import posixpath
from urllib.parse import urlsplit, urlunsplit, unquote
import markdown
from jinja2 import Template
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

# -------------------
# Config
# -------------------
markdown_dir  = 'source_docs'   # source .md directory
output_dir    = 'docs'          # where .html files go
template_file = 'page_template.html'
exclusions_file = 'exclusions.txt'
INDENT_SPACES = 2               # set to 2 if you indent sublists by 2 spaces; use 4 if you use 4

# -------------------
# Utilities
# -------------------
def slugify_basename(name: str) -> str:
    """'Sleep policies' -> 'sleep-policies' (lowercase; collapse whitespace to single dash)."""
    name = name.strip()
    name = re.sub(r'\s+', '-', name)
    return name.lower()

def get_css_path(relative_html_path: str) -> str:
    """Build relative path to CSS/main.css based on how deep the HTML file is (within docs/)."""
    depth = relative_html_path.count(os.sep)
    return '../' * depth + 'CSS/main.css'

# -------------------
# Load template & metadata
# -------------------
with open(template_file, 'r', encoding='utf-8') as f:
    template_content = f.read()
template = Template(template_content)
template_mtime = os.path.getmtime(template_file)

# Load exclusions (filenames only, e.g., "notes.md")
exclusions = set()
if os.path.exists(exclusions_file):
    with open(exclusions_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                exclusions.add(line)

# -------------------
# Markdown link adjuster: convert *.md -> slugged *.html in <a href="...">,
# slugifying directory segments too (for relative links).
# -------------------
def slugify_url_path(path: str) -> str:
    """
    Slugify each directory segment and the filename stem in a POSIX-style path.
    Keeps '.' and '..' intact.
    """
    if not path:
        return path
    dirpath, filename = posixpath.split(path)
    # slugify dir segments
    if dirpath:
        segs = []
        for seg in dirpath.split('/'):
            if seg in ('', '.', '..'):
                segs.append(seg)
            else:
                segs.append(slugify_basename(seg))
        dirpath = '/'.join(segs).strip('/')
    # slugify file stem and swap to .html
    if filename.lower().endswith('.md'):
        stem = filename[:-3]
        filename = f"{slugify_basename(stem)}.html"
    return f"{dirpath}/{filename}".strip('/') if dirpath else filename

class LinkAdjusterTreeprocessor(Treeprocessor):
    def run(self, root):
        for el in root.iter('a'):
            href = el.get('href', '')
            if not href or href.startswith(('#', '/', 'http://', 'https://', 'mailto:', 'tel:', '//')):
                continue
            parts = urlsplit(href)
            path = unquote(parts.path)
            if not path.lower().endswith('.md'):
                continue
            new_path = slugify_url_path(path)
            new_href = urlunsplit((parts.scheme, parts.netloc, new_path, parts.query, parts.fragment))
            el.set('href', new_href)

class LinkAdjusterExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(LinkAdjusterTreeprocessor(md), 'linkadjuster', 15)

# -------------------
# Nested list depth annotator (no inline styles)
# Adds class "list-depth-N" to <ul>/<ol> so CSS can style indentation.
# -------------------
class ListDepthAnnotator(Treeprocessor):
    def run(self, root):
        def annotate(node, depth):
            for child in list(node):
                if child.tag in ('ul', 'ol'):
                    cls = child.get('class', '')
                    classes = [c for c in cls.split() if c]
                    classes.append(f'list-depth-{depth}')
                    child.set('class', ' '.join(classes))
                    annotate(child, depth + 1)
                else:
                    annotate(child, depth)
        annotate(root, 0)

class ListDepthExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(ListDepthAnnotator(md), 'listdepth', 16)

# -------------------
# Main walk
# -------------------
for root, dirs, files in os.walk(markdown_dir):
    for file in files:
        if not file.endswith('.md'):
            continue

        # respect exclusions by filename
        if file in exclusions:
            print(f"Skipping excluded file: {file}")
            continue

        md_filepath = os.path.join(root, file)

        # relative path of the md file (preserve structure)
        rel_md_path = os.path.relpath(md_filepath, markdown_dir).lstrip(os.sep)

        # split into dir/name
        rel_dir, rel_name = os.path.split(rel_md_path)

        # slugify directory segments for output structure
        if rel_dir:
            slug_rel_dir = os.sep.join(
                slugify_basename(p) if p not in ('', '.', '..') else p
                for p in rel_dir.split(os.sep)
            )
        else:
            slug_rel_dir = ''

        # slugify filename (stem) and set extension to .html
        stem, _ = os.path.splitext(rel_name)
        slug = slugify_basename(stem)
        rel_html_name = f"{slug}.html"

        # assemble output relative path within docs/
        rel_html_path = os.path.join(slug_rel_dir, rel_html_name) if slug_rel_dir else rel_html_name
        html_filepath = os.path.normpath(os.path.join(output_dir, rel_html_path))

        # ensure output directory exists
        html_dir = os.path.dirname(html_filepath) or '.'
        os.makedirs(html_dir, exist_ok=True)

        # decide whether to regenerate
        regenerate = False
        if not os.path.exists(html_filepath):
            regenerate = True
        else:
            md_mtime = os.path.getmtime(md_filepath)
            html_mtime = os.path.getmtime(html_filepath)
            if md_mtime > html_mtime or template_mtime > html_mtime:
                regenerate = True

        if not regenerate:
            continue

        # read md
        with open(md_filepath, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # convert md -> html (fix links; annotate list depth)
        md_engine = markdown.Markdown(
            extensions=[LinkAdjusterExtension(), ListDepthExtension(), 'extra', 'sane_lists', 'toc'],  # 'toc' adds id="slug" to headings so #heading links work
            tab_length=INDENT_SPACES,
            output_format='html5'
        )
        html_body = md_engine.convert(md_content)

        # extract title from first "# " heading
        title = ''
        for line in md_content.splitlines():
            if line.startswith('# '):
                title = line[2:].strip()
                break

        # css path based on output html nesting (relative to docs/)
        css_path = get_css_path(rel_html_path)

        # render
        rendered_html = template.render(
            content=html_body,
            title=title,
            css_path=css_path
        )

        # write
        with open(html_filepath, 'w', encoding='utf-8') as f:
            f.write(rendered_html)
        print(f"Regenerated {html_filepath}")

