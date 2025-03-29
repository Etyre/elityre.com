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

# Load the template
with open(template_file, 'r', encoding='utf-8') as f:
    template_content = f.read()
template = Template(template_content)

# Get the modification time of the template file
template_mtime = os.path.getmtime(template_file)

# Regular expression pattern to find markdown links
markdown_link_pattern = re.compile(r'(\[.*?\])\((.*?)\)')

# Walk through all the files in the Markdown directory
for root, dirs, files in os.walk(markdown_dir):
    for file in files:
        if file.endswith('.md'):
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
                # Render the template with the content and title
                rendered_html = template.render(content=html_body, title=title)
                # Write the output HTML file
                with open(html_filepath, 'w', encoding='utf-8') as f:
                    f.write(rendered_html)
                print(f'Regenerated {html_filepath}')
