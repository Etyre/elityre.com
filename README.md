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

The nav bar lives in `nav.html` at the repo root and is inlined into every page at build time (edit it there, then rebuild). Hand-written pages such as `date.html` additionally fetch `/nav.html` at load time and swap it in, so they stay in sync without a rebuild.

The script uses the markdown library to convert .md content to HTML.

It optionally extracts a title from the first Markdown heading that starts with # .

#### Blank lines inside lists

Markdown normally treats any blank line between list items as making the whole list "loose" (every item gets paragraph spacing, including items with no blank line next to them). The script overrides this so gaps appear exactly where the source has them:

- An item preceded by one or more blank lines gets class `group-gap`, which `css/main.css` gives a top margin.
- Items with no blank line before them stay tight.
- Edit the source in a plain-text editor (e.g. iA Writer). Typora hides single blank lines between list items and rewrites them on save, so what it shows does not match the file.
- Blank lines before an indented paragraph (a multi-paragraph item) or before non-list text behave as normal Markdown.

### Template Integration

The script reads a Jinja2 template (e.g., page_template.html).

The placeholders {{ title }} and {{ content }} are replaced with the extracted title and the converted HTML body, respectively.

The final rendered HTML is then saved to the output directory, preserving subdirectories as needed.

#### Directory Creation

If any subdirectories are needed to mirror the original Markdown structure, the script creates them automatically in the output directory (avoiding errors for empty directory names).

#### Console Output

The script prints messages indicating when files are skipped due to exclusion and when files are regenerated due to changes.

#### Heading links and table of contents

Every heading gets an `id` slugified from its text (`## What I Want` → `#what-i-want`), so you can link to a specific section of a page.

Put `<TOC>` on its own line in a markdown file to insert a linked table of contents of that page's `##`-and-deeper headings.
