import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/staples/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created")

    def on_modified(self, event):
        print(f"{event.src_path} has been modified")

    def on_moved(self, event):
        print(f"Directory moved/renamed: {event.src_path} to {event.dest_path}")

    def on_deleted(self, event):
        print(f"Oops! {event.src_path} has been deleted")

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, path=from_dir, recursive=True)
observer.start()

try:
    print(f"Watching for changes in {from_dir}. Press any key to stop.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    observer.join()
    print("Observer stopped.")
