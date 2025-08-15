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
markdown_dir = 'source_docs'   # source .md directory
output_dir   = 'docs'                  # where .html files go
template_file = 'page_template.html'
exclusions_file = 'exclusions.txt'
HTML_EXT = 'html'                   # set to 'hml' if you really want .hml

# -------------------
# Utilities
# -------------------
def slugify_basename(name: str) -> str:
    """
    Turn 'Sleep policies' -> 'sleep-policies'
    (Lowercases; collapses any whitespace to a single dash.)
    """
    name = name.strip()
    name = re.sub(r'\s+', '-', name)
    return name.lower()

def slugify_path_segments(path: str, *, is_file=False) -> str:
    """
    Slugify each non-dot segment in a POSIX-style path.
    If is_file=True, slugify the stem and keep extension as-is handled outside.
    Keeps '.' and '..' untouched; ignores empty segments.
    """
    segs = [s for s in path.split('/')]

    # For directory segments
    for i, seg in enumerate(segs[:-1] if is_file else segs):
        if seg in ('', '.', '..'):
            continue
        segs[i] = slugify_basename(seg)

    return '/'.join(segs)

def get_css_path(relative_html_path: str) -> str:
    """
    Build correct relative path to CSS/main.css based on how deep the HTML file is.
    """
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
# slugifying directory segments too.
# -------------------
class LinkAdjusterTreeprocessor(Treeprocessor):
    def run(self, root):
        for el in root.iter('a'):
            href = el.get('href', '')
            if not href or href.startswith(('#', '/', 'http://', 'https://', 'mailto:', 'tel:', '//')):
                continue

            parts = urlsplit(href)
            path = unquote(parts.path)  # decode %20 etc for consistent slugging
            if not path.lower().endswith('.md'):
                continue

            # Split into dir and file; slugify dir segments
            dirpath, filename = posixpath.split(path)
            dirpath = slugify_path_segments(dirpath)

            # Slugify file stem and swap extension
            stem = filename[:-3]  # drop ".md"
            new_stem = slugify_basename(stem)
            new_filename = f"{new_stem}.{HTML_EXT}"

            new_path = posixpath.join(dirpath, new_filename) if dirpath else new_filename
            new_href = urlunsplit((parts.scheme, parts.netloc, new_path, parts.query, parts.fragment))
            el.set('href', new_href)

class LinkAdjusterExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(LinkAdjusterTreeprocessor(md), 'linkadjuster', 15)

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
            slug_rel_dir = os.sep.join(slugify_basename(p) for p in rel_dir.split(os.sep))
        else:
            slug_rel_dir = ''

        # slugify filename (stem) and set extension
        stem, _ = os.path.splitext(rel_name)
        slug = slugify_basename(stem)
        rel_html_name = f"{slug}.{HTML_EXT}"

        # assemble output relative path
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

        # convert md -> html (and fix intra-site .md links to slugged .html + dirs)
        html_body = markdown.markdown(md_content, extensions=[LinkAdjusterExtension()])

        # extract title from first "# " heading
        title = ''
        for line in md_content.splitlines():
            if line.startswith('# '):
                title = line[2:].strip()
                break

        # css path based on output html nesting
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


