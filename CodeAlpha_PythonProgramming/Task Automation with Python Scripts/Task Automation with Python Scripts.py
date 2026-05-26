import os
import shutil

source_folder = r"C:\Users\nisch\OneDrive\Pictures"
destination_folder = "moved_images"

os.makedirs(destination_folder, exist_ok=True)

files = os.listdir(source_folder)

for file in files:
    if file.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(f"Moved: {file}")

print("All JPG files moved successfully!")
