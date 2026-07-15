import os
import shutil
from pathlib import Path

def organize_folder(folder_path):
    extensions = {
        'Images': ['.jpg', '.png', '.jpeg', '.gif'],
        'Docs': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Code': ['.py', '.java', '.cpp', '.c'],
        'Zips': ['.zip', '.rar', '.7z']
    }

    for filename in os.listdir(folder_path):
        for folder, exts in extensions.items():
            if any(filename.endswith(ext) for ext in exts):
                folder_dir = os.path.join(folder_path, folder)
                os.makedirs(folder_dir, exist_ok=True)
                shutil.move(os.path.join(folder_path, filename), folder_dir)
                break

organize_folder(r"C:\Users\YourName\Downloads")
print("Folder organized!")
