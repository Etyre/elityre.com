# elityre.com

This repo includes everything to generate my personal website, including markdown files and a python script that converts those markdown files into html.

## The markdown to html script

To run the script, simply enter `python generate_html.py` in the terminal.

### Additional details about the script

#### Directory Traversal

The script scans the specified markdown_dir (e.g., markdown_content) for all files ending in .md.

It preserves directory structure when generating corresponding .html files in the specified output_dir.

#### Exclusions File

A text file (exclusions.txt) contains a list of Markdown filenames to skip.

Any file listed here is excluded from HTML generation or updates.

#### File Regeneration Logic

The script creates an HTML file if it doesn’t already exist.

If the HTML file does exist, it checks:

- The modification time of the Markdown file

- The modification time of the template file

- The modification time of the existing HTML file

If the Markdown file or template is more recent than the HTML file, the HTML file is regenerated.

If the HTML file is up to date (and the template and Markdown haven’t changed), it is left as is.

#### Link Rewriting

Before conversion, the script scans the Markdown text for links to other Markdown files in the same project (i.e., links ending in .md that are not external or absolute).

These links have their .md extension replaced with .html, so that references among Markdown files become proper references among HTML files.

#### Markdown to HTML Conversion

The script uses the markdown library to convert .md content to HTML.

It optionally extracts a title from the first Markdown heading that starts with # .

### Template Integration

The script reads a Jinja2 template (e.g., page_template.html).

The placeholders {{ title }} and {{ content }} are replaced with the extracted title and the converted HTML body, respectively.

The final rendered HTML is then saved to the output directory, preserving subdirectories as needed.

#### Directory Creation

If any subdirectories are needed to mirror the original Markdown structure, the script creates them automatically in the output directory (avoiding errors for empty directory names).

#### Console Output

The script prints messages indicating when files are skipped due to exclusion and when files are regenerated due to changes.
