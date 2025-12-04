import os

def remove_download_from_all_files(folder_path: str):
    # Loop through everything in the folder
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)

        # Skip folders
        if os.path.isdir(old_path):
            continue

        # If ".download" is in the filename
        if ".download" in filename:
            new_name = filename.replace(".download", "")
            new_path = os.path.join(folder_path, new_name)

            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {filename}  →  {new_name}")

 
remove_download_from_all_files("C:/Users/DELL/Downloads/fake-crypto-sender-main/django/project/static/main/")
