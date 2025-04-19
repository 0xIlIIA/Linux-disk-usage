import os
import sys

def get_folder_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            try:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
            except Exception as e:
                print(f"Error reading file: {fp}, skipping. ({e})")
    return total_size

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py /path/to/folder")
        sys.exit(1)

    folder_path = sys.argv[1]

    if not os.path.exists(folder_path):
        print("Error: Path does not exist.")
        sys.exit(1)

    size_bytes = get_folder_size(folder_path)
    size_mb = size_bytes / (1024 * 1024)
    print(f"Total size of '{folder_path}': {size_mb:.2f} MB")
