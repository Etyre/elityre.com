"""
Watch source_docs/ (plus page_template.html and nav.html) and re-run generate_html.py
whenever a markdown file is saved.

Run by hand:   .venv/bin/python watch_and_build.py
Or in the background via launchd: see com.elityre.elityre-site-watcher.plist
"""
import os
import re
import subprocess
import sys
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

ROOT = os.path.dirname(os.path.abspath(__file__))
PYTHON = sys.executable
GENERATOR = os.path.join(ROOT, 'generate_html.py')
WATCH_DIR = os.path.join(ROOT, 'source_docs')
IMAGES_DIR = os.path.join(WATCH_DIR, 'images')
TEMPLATE = os.path.join(ROOT, 'page_template.html')
NAV = os.path.join(ROOT, 'nav.html')
ALIASES = os.path.join(ROOT, 'aliases.txt')
DEBOUNCE_SECONDS = 0.5   # editors often write a file in several steps; wait for them to settle


def build():
    print(time.strftime('%Y-%m-%d %H:%M:%S'), 'building...', flush=True)
    result = subprocess.run([PYTHON, GENERATOR], cwd=ROOT, capture_output=True, text=True)
    out = (result.stdout + result.stderr).strip()
    if out:
        print(out, flush=True)
    print('done (exit %d)' % result.returncode, flush=True)


def slugify(name):
    """Must match slugify_basename in generate_html.py."""
    return re.sub(r'\s+', '-', name.strip()).lower()


# Renaming a brand-new "Untitled" note to its real name isn't a URL change worth aliasing.
UNTITLED_RE = re.compile(r'^untitled ?\d*$', re.I)


def record_rename(src_path, dest_path):
    """A markdown file was renamed: record the old URL in aliases.txt so the old
    page keeps being generated (and update any older aliases that pointed at the
    old filename, so chains of renames keep working)."""
    old_stem = os.path.splitext(os.path.basename(src_path))[0]
    old_name = os.path.basename(src_path)
    new_name = os.path.basename(dest_path)
    if slugify(old_stem) == slugify(os.path.splitext(new_name)[0]):
        return  # same slug, same URL: nothing to do
    if UNTITLED_RE.match(old_stem):
        return
    lines = []
    if os.path.exists(ALIASES):
        with open(ALIASES, encoding='utf-8') as f:
            lines = f.read().splitlines()
    # re-point older aliases that mapped to the old filename
    changed = False
    for i, line in enumerate(lines):
        if '->' in line and not line.strip().startswith('#'):
            left, _, right = line.partition('->')
            if right.strip() == old_name:
                lines[i] = f"{left.strip()} -> {new_name}"
                changed = True
    new_line = f"{slugify(old_stem)} -> {new_name}"
    if new_line not in [l.strip() for l in lines]:
        lines.append(new_line)
        changed = True
    if changed:
        with open(ALIASES, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines) + '\n')
        print(time.strftime('%Y-%m-%d %H:%M:%S'),
              f'recorded rename in aliases.txt: {new_line}', flush=True)


class Handler(FileSystemEventHandler):
    def __init__(self):
        self.pending_since = None

    def on_moved(self, event):
        src = event.src_path
        dest = getattr(event, 'dest_path', '') or ''
        if (not event.is_directory
                and src.endswith('.md') and dest.endswith('.md')
                and os.path.abspath(src).startswith(WATCH_DIR + os.sep)
                and os.path.abspath(dest).startswith(WATCH_DIR + os.sep)):
            record_rename(src, dest)

    def on_any_event(self, event):
        if event.is_directory:
            return
        paths = [event.src_path, getattr(event, 'dest_path', '')]
        if any(p.endswith('.md')
               or os.path.abspath(p) in (TEMPLATE, NAV, ALIASES)
               or os.path.abspath(p).startswith(IMAGES_DIR + os.sep)
               for p in paths if p):
            self.pending_since = time.time()


if __name__ == '__main__':
    build()  # catch anything that changed while the watcher wasn't running
    handler = Handler()
    observer = Observer()
    observer.schedule(handler, WATCH_DIR, recursive=True)
    observer.schedule(handler, ROOT, recursive=False)  # for page_template.html
    observer.start()
    print('watching', WATCH_DIR, 'and', TEMPLATE, flush=True)
    try:
        while True:
            time.sleep(0.2)
            if handler.pending_since and time.time() - handler.pending_since >= DEBOUNCE_SECONDS:
                handler.pending_since = None
                build()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
