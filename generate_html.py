import os
import re
import markdown
from jinja2 import Template

# Specify the directory containing the Markdown files
markdown_dir = 'source_docs'  # Update with your directory path

# Specify the output directory for HTML files
output_dir = 'docs'  # Adjust if HTML files should be in a different directory

# Path to the template HTML file
template_file = 'page_template.html'

# Path to the exclusions file
exclusions_file = 'exclusions.txt'

# Load the template
with open(template_file, 'r', encoding='utf-8') as f:
    template_content = f.read()
template = Template(template_content)

# Get the modification time of the template file
template_mtime = os.path.getmtime(template_file)

# Load exclusions
exclusions = set()
if os.path.exists(exclusions_file):
    with open(exclusions_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                exclusions.add(line)

# Regular expression pattern to find markdown links
markdown_link_pattern = re.compile(r'(\[.*?\])\((.*?)\)')

def get_css_path(relative_path: str) -> str:
    """
    Given the relative path of the Markdown file (relative to `markdown_dir`),
    determine how many directories deep it is, then return the correct
    relative path to 'CSS/main.css'.
    """
    # Count how many folder separators are in the relative path
    depth = relative_path.count(os.sep)
    # Build something like '../../CSS/main.css' if depth=2
    return '../' * depth + 'CSS/main.css'

# Walk through all the files in the Markdown directory
for root, dirs, files in os.walk(markdown_dir):
    for file in files:
        if file.endswith('.md'):
            # Skip excluded files
            if file in exclusions:
                print(f"Skipping excluded file: {file}")
                continue

            md_filepath = os.path.join(root, file)
            # Determine the relative path from the markdown directory
            relative_path = os.path.relpath(md_filepath, markdown_dir)
            relative_path = relative_path.lstrip(os.sep)
            # Construct the output filename
            html_filename = os.path.splitext(relative_path)[0] + '.html'
            html_filepath = os.path.normpath(os.path.join(output_dir, html_filename))

            # Create directories in output_dir if they don't exist
            html_dir = os.path.dirname(html_filepath)
            if not html_dir:
                html_dir = '.'
            if not os.path.exists(html_dir):
                os.makedirs(html_dir)

            # Check if HTML file needs to be regenerated
            regenerate = False
            if not os.path.exists(html_filepath):
                regenerate = True
            else:
                # Compare modification times
                md_mtime = os.path.getmtime(md_filepath)
                html_mtime = os.path.getmtime(html_filepath)
                if md_mtime > html_mtime or template_mtime > html_mtime:
                    regenerate = True

            if regenerate:
                # Read Markdown content
                with open(md_filepath, 'r', encoding='utf-8') as f:
                    md_content = f.read()

                # Convert links to other markdown files to html links
                def replace_md_links(match):
                    text = match.group(1)
                    url = match.group(2)
                    # Check if url ends with .md and is a relative link
                    if url.endswith('.md') and not url.startswith(('http://', 'https://', '/')):
                        # Replace .md with .html
                        new_url = os.path.splitext(url)[0] + '.html'
                        return f'{text}({new_url})'
                    else:
                        # Leave the link unchanged
                        return match.group(0)

                md_content = re.sub(markdown_link_pattern, replace_md_links, md_content)

                # Convert Markdown to HTML
                html_body = markdown.markdown(md_content)

                # Optional: Extract title from the first heading
                lines = md_content.splitlines()
                title = ''
                for line in lines:
                    if line.startswith('# '):
                        title = line.lstrip('# ').strip()
                        break

                # Determine the relative CSS path based on nesting level
                css_path = get_css_path(relative_path)

                # Render the template with the content, title, and css path
                rendered_html = template.render(
                    content=html_body,
                    title=title,
                    css_path=css_path
                )

                # Write the output HTML file
                with open(html_filepath, 'w', encoding='utf-8') as f:
                    f.write(rendered_html)
                print(f'Regenerated {html_filepath}')
