'''
simple script to remove metadata from all files
'''

import os
from mutagen import File

ROOT_DIR = "./SAMPLES"

for root, dirs, files in os.walk(ROOT_DIR):
    for name in files:
        path = os.path.join(root, name)

        try:
            audio = File(path, easy=False)

            if audio is None:
                print(f"Skipping unsupported file: {path}")
                continue

            if audio.tags:
                audio.delete()
                audio.save()
                print(f"Metadata removed: {path}")
            else:
                print(f"No metadata found: {path}")

        except Exception as e:
            print(f"Error processing {path}: {e}")

print("End.")
