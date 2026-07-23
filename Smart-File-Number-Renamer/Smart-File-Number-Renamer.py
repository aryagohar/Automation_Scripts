"""
Smart File Number Renamer

Renames numbered files by filling gaps in sequential file numbering while
preserving the original filename format.

Features:
- Supports filenames with leading numbers (e.g., 001report.pdf).
- Supports filenames with trailing numbers (e.g., report001.exe).
- Preserves the original number width using leading zeros.
- Processes all matching files recursively in the specified folder.
- Renames only files matching the supported filename patterns.

Examples:
    report001.pdf   -> report001.pdf
    report003.txt   -> report002.txt

    001report.pdf   -> 001report.pdf
    003report.pdf   -> 002report.pdf
"""

import os
import re
import shutil
import sys
from pathlib import Path


def smart_file_number_renamer(target_folder: Path | str, number_position: str) -> None:
    target_folder = Path(target_folder)     # Make sure folder is a Path object, not string.

    # Compile needed regexes
    begin_pattern = re.compile(r'^\d+[A-Za-z][A-Za-z0-9_ -]*\.[A-Za-z0-9]+$')
    end_pattern = re.compile(r'^[A-Za-z][A-Za-z0-9_ -]*\d+\.[A-Za-z0-9]+$')
    leading_digits_pattern = re.compile(r'\d+')
    trailing_digits_pattern = re.compile(r'(\d+)(?!.*\d)')

    # Walk the entire folder tree and rename files having gaps in their numbers.
    for folder_name, _, filenames in os.walk(target_folder):
        current_folder = Path(folder_name)
        counter = 0
        stem = ""
        current_number = ""
        previous_number = ""
        for filename in sorted(filenames):
            if number_position.upper() == 'B':
                # filename examples: 0350spam.txt  129exa38mple.exe
                file = begin_pattern.fullmatch(filename)
            else:
                # filename examples: spam03565.txt  exa38mple0012.exe
                file = end_pattern.fullmatch(filename)
            if file:
                file_name = file.group()
                stem = Path(file_name).stem
                if number_position.upper() == 'B':
                    # Fetch leading digits in fn
                    match = re.match(leading_digits_pattern, stem)
                    current_number = match.group()
                    pref_len = len(current_number)
                else:
                    # Fetch trailing digits in fn
                    match = re.search(trailing_digits_pattern, stem)
                    current_number = match.group(1)
                    pref_len = len(current_number)
                if counter > 0:
                    if int(current_number) - int(previous_number) == 1:
                        previous_number = current_number
                        continue
                    else:
                        if number_position.upper() == 'B':
                            new_fn = re.sub(leading_digits_pattern, str(int(previous_number) + 1).zfill(pref_len), filename)
                        else:
                            new_fn = re.sub(trailing_digits_pattern, str(int(previous_number) + 1).zfill(pref_len), filename)
                        source = current_folder / file_name
                        destination = current_folder / new_fn
                        if destination.exists():
                            print(f"Skipped: '{destination}' already exists.")
                        else:
                            # Renaming the file
                            shutil.move(source, destination)
                        previous_number = str(int(previous_number) + 1).zfill(pref_len)
                else:
                    previous_number = current_number
                    counter += 1
                    continue

def main():
    folder = input('Enter folder full path: ')
    # Check input path exists as a folder
    if not Path(folder).is_dir():
        sys.exit(f"Error: '{folder}' does not exist or is not a directory.")

    while True:
        num_position = input(
            r'Where is number position in file names: beginning(001example.txt) or end(exa6mple001.txt)? (b / e): ')
        if num_position.upper() != 'B' and num_position.upper() != 'E':
            continue
        else:
            break

    smart_file_number_renamer(folder, num_position)
    
    input("\nFinished. Press Enter to exit...")



if __name__ == "__main__":
    main()





