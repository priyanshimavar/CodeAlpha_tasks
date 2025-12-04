import os
import shutil

# --- Configuration ---
SOURCE_DIR = "./source_images"
DEST_DIR = "./destination_images"
# ---------------------

# Ensure destination directory exists
if not os.path.exists(DEST_DIR):
    os.makedirs(DEST_DIR)
    print(f"Created destination directory: {DEST_DIR}")

print(f"Scanning source directory: {SOURCE_DIR}")
files_moved_count = 0

if not os.path.exists(SOURCE_DIR):
    print(f"Source directory not found: {SOURCE_DIR}")
else:
    for filename in os.listdir(SOURCE_DIR):
        # Check for JPG or JPEG extension (case insensitive)
        if filename.lower().endswith((".jpg", ".jpeg")):
            source_path = os.path.join(SOURCE_DIR, filename)
            dest_path = os.path.join(DEST_DIR, filename)

            if os.path.isfile(source_path):
                try:
                    shutil.move(source_path, dest_path)
                    print(f"Moved: {filename}")
                    files_moved_count += 1
                except shutil.Error as e:
                    print(f"Error moving {filename}: {e}")

print(f"\nOperation complete. Total files moved: *{files_moved_count}*")