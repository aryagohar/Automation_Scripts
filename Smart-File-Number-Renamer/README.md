# Smart File Number Renamer

[![Python Version](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)

[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)]()

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[![Status](https://img.shields.io/badge/Status-Active-success)]()

[![GitHub release](https://img.shields.io/github/v/release/aryagohar/Automation_Scripts)](https://github.com/aryagohar/Automation_Scripts/releases)

[![Downloads](https://img.shields.io/github/downloads/aryagohar/Automation_Scripts/total)](https://github.com/aryagohar/Automation_Scripts/releases)

[![Repo Size](https://img.shields.io/github/repo-size/aryagohar/Automation_Scripts)](https://github.com/aryagohar/Automation_Scripts)

[![Last Commit](https://img.shields.io/github/last-commit/aryagohar/Automation_Scripts)](https://github.com/aryagohar/Automation_Scripts)

[![Stars](https://img.shields.io/github/stars/aryagohar/Automation_Scripts?style=social)](https://github.com/aryagohar/Automation_Scripts)

[Python](https://www.python.org/)

A lightweight Python utility that automatically **renames numbered files
by filling gaps in sequential numbering** while preserving the original
filename format and leading zeros.

The utility works recursively through all subfolders of a specified
directory and supports filenames whose numbers appear either at the
**beginning** or at the **end** of the filename as user selects.

------------------------------------------------------------------------

## Features

- Renames files recursively in all subdirectories.
- Supports filenames with **leading numbers**.
- Supports filenames with **trailing numbers**.
- Preserves the original number width by keeping leading zeros.
- Skips files that do not match the supported filename patterns.
- Detects filename conflicts and safely skips existing destination
  files.
- Uses only Python's standard library.

------------------------------------------------------------------------

## Download

If you do not want to run the Python script, you can download the
standalone executable from the repository's **Releases** section.

> **Executable available:** `Smart-File-Number-Renamer``-v1.0.0``.exe`

------------------------------------------------------------------------

## Requirements

- Python 3.10 or later

No third-party packages are required.

------------------------------------------------------------------------

## Usage

Run the script:

    python smart_file_number_renamer.py

The program asks for:

1.  Folder path
2.  Number position

<!-- -->

    Enter folder full path:

Example:

    D:\Books

Then choose:

    Where is number position in file names:
    beginning (001example.txt)
    or
    end (example001.txt)

    (b / e):

- **b/B** → numbers at the beginning of filename
- **e/E** → numbers at the end of filename

## Supported Filename Patterns

### Beginning numbering

Examples:

    001Report.pdf
    010Book.epub
    005p - Book.epub
    123Example.txt

Regex:

    ^\d+[A-Za-z][A-Za-z0-9_ -]*\.[A-Za-z0-9]+$

------------------------------------------------------------------------

### Ending numbering

Examples:

    Report001.pdf
    Book010.epub 
    Book_me - we010.epub
    Example123.txt

Regex:

    ^[A-Za-z][A-Za-z0-9_ -]*\d+\.[A-Za-z0-9]+$

------------------------------------------------------------------------

## Before / After Examples

### Beginning numbers

Before

    001Report.pdf
    002Report.pdf
    004Report.pdf
    007Report.pdf

After

    001Report.pdf
    002Report.pdf
    003Report.pdf
    004Report.pdf

### Ending numbers

Before

    Report001.pdf
    Report002.pdf
    Report005.pdf
    Report007.pdf

After

    Report001.pdf
    Report002.pdf
    Report003.pdf
    Report004.pdf

------------------------------------------------------------------------

## Example Output

Successful execution

    Enter folder full path:
    D:\Books

    Where is number position in file names:
    beginning(001example.txt) or end(example001.txt)? (b / e):

    b

If a destination filename already exists

    Skipped:
    'D:\Books\003Report.pdf' already exists.

------------------------------------------------------------------------

## How It Works

For every folder in the directory tree:

1.  Reads all filenames.
2.  Sorts them alphabetically.
3.  Finds files matching the selected filename pattern.
4.  Extracts the numbering portion.
5.  Detects numbering gaps.
6.  Renames files to make the sequence consecutive.
7.  Preserves leading zeros.
8.  Continues recursively through all subfolders.

------------------------------------------------------------------------

## Limitations

- Files are processed in **alphabetical order**.
- Only filenames matching the supported patterns are renamed.
- Exactly one numbering location is supported per execution (beginning
  **or** end).
- Files that would overwrite an existing filename are skipped.
- Extensions are preserved exactly as they are.

------------------------------------------------------------------------

## Technologies Used

- Python
- pathlib
- os.walk()
- shutil
- regular expressions (`re`)

------------------------------------------------------------------------

## Project Structure

    Smart-File-Number-Renamer/
    │
    ├── smart_file_number_renamer.py
    ├── README.md
    └── LICENSE

------------------------------------------------------------------------

## License

This project is licensed under the MIT License.

------------------------------------------------------------------------

## Author

**Aryagohar**

If you find this project useful, consider giving the repository a ⭐ on
GitHub.
