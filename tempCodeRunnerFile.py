import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:

    def __init__(self, directory_to_watch, directories_to_create):
        self.directory_to_watch = directory_to_watch
        self.directories_to_create = directories_to_create

    def run(self):
        event_handler = Handler(self.directories_to_create)
        observer = Observer()
        observer.schedule(event_handler, self.directory_to_watch, recursive=False)
        observer.start()
        try:
            while True:
                time.sleep(5)
                print("stuck")
        except:
            observer.stop()
        observer.join()

class Handler(FileSystemEventHandler):

    def __init__(self, directories_to_create):
        self.directories_to_create = directories_to_create

   
    def on_created(self, event):
        if not event.is_directory:
            self.sort_file(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.sort_file(event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            self.sort_file(event.dest_path)  # Use dest_path for 'moved' events

    def sort_file(self, source_file_path):
        filename, extension = os.path.splitext(source_file_path)
        extension = extension.lower() 

        if not os.path.isfile(source_file_path):
            print(f"Warning: Skipping '{filename}' - Not a valid file or no longer exists.")
            return 

        for category, extensions in self.directories_to_create.items():
            if extension in extensions:
                destination_dir = os.path.join(os.path.expanduser("~"), "Desktop", category)
                os.makedirs(destination_dir, exist_ok=True) 

                destination_file_path = os.path.join(destination_dir, os.path.basename(source_file_path))

                try:
                    shutil.move(source_file_path, destination_file_path)
                    print(f"Moved '{filename}' to '{destination_dir}'")
                except shutil.Error as e: 
                    print(f"Error moving '{filename}': {e}")
                break 
        else: # No matching category found
            print(f"Warning: No category found for '{filename}' (extension '{extension}'). File not moved.")


if __name__ == "__main__":
    watch_directory = os.path.join(os.path.expanduser("~"), "Downloads") 
    category_mapping = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.doc', '.docx', '.pdf', '.txt', '.xlsx', '.pptx'],
        'Audio': ['.mp3', '.wav', '.flac'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        # Add more categories as needed
    }
    w = Watcher(watch_directory, category_mapping)
    w.run()