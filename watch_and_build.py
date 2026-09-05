"""
Watch source_docs/ (plus page_template.html and nav.html) and re-run generate_html.py
whenever a markdown file is saved.

Run by hand:   .venv/bin/python watch_and_build.py
Or in the background via launchd: see com.elityre.elityre-site-watcher.plist
"""
import os
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
DEBOUNCE_SECONDS = 0.5   # editors often write a file in several steps; wait for them to settle


def build():
    print(time.strftime('%Y-%m-%d %H:%M:%S'), 'building...', flush=True)
    result = subprocess.run([PYTHON, GENERATOR], cwd=ROOT, capture_output=True, text=True)
    out = (result.stdout + result.stderr).strip()
    if out:
        print(out, flush=True)
    print('done (exit %d)' % result.returncode, flush=True)


class Handler(FileSystemEventHandler):
    def __init__(self):
        self.pending_since = None

    def on_any_event(self, event):
        if event.is_directory:
            return
        paths = [event.src_path, getattr(event, 'dest_path', '')]
        if any(p.endswith('.md')
               or os.path.abspath(p) in (TEMPLATE, NAV)
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
