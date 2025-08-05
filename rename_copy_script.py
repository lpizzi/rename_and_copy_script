import os
import json
import argparse
import shutil
from datetime import datetime

def list_and_copy_json_files(folder_path):
    files_with_timestamps = []
    dest_folder = os.path.join(folder_path, "renamed_copies")

    # Create destination subfolder if it doesn't exist
    os.makedirs(dest_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    ts = data.get('created_timestamp')
                    if ts is not None:
                        files_with_timestamps.append((filename, ts))
                        # Prepare new filename
                        hr_date = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d_%H-%M')
                        new_filename = f"{hr_date}_{filename}"
                        dest_path = os.path.join(dest_folder, new_filename)
                        shutil.copy2(file_path, dest_path)
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    # Sort files by timestamp
    files_with_timestamps.sort(key=lambda x: x[1])

    print("Sorted files (original names) with human-readable timestamps:")
    for filename, ts in files_with_timestamps:
        hr_date = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M')
        print(f"{filename}: {hr_date}")

    print(f"\nRenamed copies created in: {dest_folder}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="List and copy JSON files by created_timestamp.")
    parser.add_argument("folder_path", help="Path to the folder containing .json files")
    args = parser.parse_args()

    list_and_copy_json_files(args.folder_path)
