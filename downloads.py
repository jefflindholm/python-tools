import os
from collections import defaultdict
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler




downloads_path = os.path.expanduser('~/Downloads')


# Count file types in Downloads folder
file_types = defaultdict(int)

for file in files:
    ext = os.path.splitext(file)[1]
    file_types[ext] += 1

for ext, count in file_types.items():
    print(f"{ext}: {count}")

# Create folders for different file categories
categories = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Archives': ['.zip', '.rar', '.tar'],
    'Executables': ['.exe', '.dmg', '.sh'],
    'Code': ['.py', '.cpp', '.js'],
    'Others': []
}

for category in categories:
    folder_path = os.path.join(downloads_path, category)
    os.makedirs(folder_path, exist_ok=True)

# Move files to respective folders
for file in files:
    file_path = os.path.join(downloads_path, file)
    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()
        moved = False
        for category, extensions in categories.items():
            if ext in extensions:
                shutil.move(file_path, os.path.join(downloads_path, category, file))
                moved = True
                break
        if not moved:
            shutil.move(file_path, os.path.join(downloads_path, 'Others', file))


# Clean up junk files in Downloads folder
trash_exts = ['.tmp', '.part', '.crdownload', '.ds_store']

deleted_count = 0

for root, _, files in os.walk(downloads_path):
    for file in files:
        if os.path.splitext(file)[1].lower() in trash_exts:
            os.remove(os.path.join(root, file))
            deleted_count += 1

print(f"🧹 Deleted {deleted_count} junk files.")


# Watch for new files in Downloads folder and auto-sort them
class AutoSortHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            ext = os.path.splitext(filename)[1].lower()
            for category, extensions in categories.items():
                if ext in extensions:
                    shutil.move(event.src_path, os.path.join(downloads_path, category, filename))
                    return
            shutil.move(event.src_path, os.path.join(downloads_path, 'Others', filename))

observer = Observer()
observer.schedule(AutoSortHandler(), downloads_path, recursive=False)
observer.start()