"""
Find duplicate filenames recursively in a folder tree.

The comparison is case-insensitive to match Windows filename behavior.
The script reports duplicate filenames and their full paths but does not
modify any files.
"""

import os
import sys
from pathlib import Path


def smart_duplicate_filename_finder(target_folder: Path | str) -> None:
    target_folder = Path(target_folder)     # Make sure folder is a Path object, not string.
    main_dict = {}
    folders_scanned = 0
    files_scanned = 0
    LRM = '\u200E'
    counter = 0
    print("\033[33mScanning, Please wait...\033[0m", flush=True)

    # Walk the folder tree and collect filenames for duplicate detection.
    for folder_name, _, filenames in os.walk(target_folder):
        current_folder = Path(folder_name)
        folders_scanned += 1
        # Only display the last 70 chars of the path
        if len(str(current_folder)) > 70:
            display_folder = fr"...\{str(current_folder)[-70:]}"
        else:
            display_folder = str(current_folder)
        for filename in filenames:
            files_scanned += 1
            counter += 1
            # Update live status display after every 150 files scanned
            if counter == 150:
                print(f"\r{LRM + display_folder}" + " " * 10, end="", flush=True)
                counter = 0
            if filename.casefold() in main_dict:
                main_dict[filename.casefold()].append(str(current_folder / filename))
            else:
                main_dict[filename.casefold()] = [str(current_folder / filename)]
    print()
    duplicates = {k:v for k, v in main_dict.items() if len(v) > 1}
    if duplicates:
        sorted_duplicates = dict(sorted(duplicates.items(), key=lambda x: x[0]))
        print("\033[31mDuplicate filenames found in the given folder:\033[0m\n")
        save_file = input("Save the list of duplicate filenames to dup_file_list000.txt file? (y/n): ")
        if save_file.lower() == 'y':
            path_string = ""
            with open(f"dup_file_list000.txt", "a", encoding="utf-8") as f:
                for filename,paths in sorted_duplicates.items():
                    path_string =""
                    print(f"\033[33m{LRM + filename}: {len(paths)} occurrences\033[0m")
                    for path in sorted(paths):
                        print('    ', LRM + path)
                        path_string += "    " + f"{str(path)}\n"
                    path_string += '\n'
                    write_content = f"{filename}:\n" + path_string
                    f.write(write_content.strip()+"\n")
        else:
            for filename, paths in sorted_duplicates.items():
                print(f"\033[33m{LRM + filename}: {len(paths)} occurrences\033[0m")
                for path in sorted(paths):
                    print('    ', LRM + path)
    else:
        print("\033[32mNo duplicates found in the given folder.\033[0m")

    print(f"\033[33mFolders scanned: {folders_scanned:,}\033[0m")
    print(f"\033[33mFiles scanned: {files_scanned:,}\033[0m")
    print(f"\033[33mDuplicate filenames: {len(duplicates):,}\033[0m")


def main():
    print("""
    Note: Filename comparison is case-insensitive (Windows behavior).
    On case-sensitive file systems (e.g., most Linux systems), filenames
    differing only by letter case will be reported as duplicates.
    """)
    folder = input('Enter folder full path: ')
    # Check input path exists as a folder
    if not Path(folder).is_dir():
        sys.exit(f"Error: '{folder}' does not exist or is not a directory.")

    smart_duplicate_filename_finder(folder)

    input("\n\033[31mFinished. Press Enter to exit...\033[0m\n")


if __name__ == "__main__":
    main()





