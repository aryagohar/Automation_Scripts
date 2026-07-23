# Smart Duplicate Filename Finder

[![Python Version](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)

![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

![License](https://img.shields.io/badge/License-MIT-green.svg)

![Status](https://img.shields.io/badge/Status-Active-success)

[![GitHub Release](https://img.shields.io/github/v/release/aryagohar/Automation_Scripts)](https://github.com/aryagohar/Automation_Scripts/releases)

[![Downloads](https://img.shields.io/github/downloads/aryagohar/Automation_Scripts/total)](https://github.com/aryagohar/Automation_Scripts/releases)

A lightweight Python utility that **recursively scans a folder tree and finds duplicate filenames**.

The utility compares filenames **case-insensitively** (matching Windows filename behavior), reports every duplicate filename together with all of its locations, and **never modifies any files**.

> **Windows executable (.exe)** is available in the **Releases** section of this repository.

---

## Features

- Recursively scans all folders and subfolders.
- Detects duplicate filenames anywhere in the selected folder tree.
- Uses **case-insensitive** filename comparison (Windows behavior).
- Correctly displays file paths containing **mixed English (LTR)** and **Persian/Arabic (RTL)** characters.
- Displays the **currently scanned folder** while processing.
- Reports every location where each duplicate filename exists.
- Write the list of duplicate filenames to dup_file_list000.txt file if user confirms it
- Displays summary statistics after scanning.
- Uses only Python's standard library.
- Never renames, moves, or deletes files.

---

## Supported Platforms

- ✅ Windows (recommended)
- ✅ Linux*
- ✅ macOS

\* See the Linux note below.

---

## Linux Note

This utility intentionally performs **case-insensitive** filename comparison to match Windows behavior.

On case-sensitive file systems (such as most Linux installations), filenames differing only by letter case will be reported as duplicates.

Example:

```
Report.pdf
REPORT.pdf
report.pdf
```

Windows treats these as the same filename, while Linux treats them as different files.

---

## Requirements

- Python 3.10 or newer

No third-party packages are required.

---

## Usage

Run the script:

```bash
python smart_duplicate_filename_finder.py
```

Enter the folder to scan:

```
Enter folder full path:
D:\Documents
```

During scanning, the utility continuously displays the folder currently being processed:

```
Scanning, Please wait...

D:\Documents\Projects\Python
```

---

## Example Directory

```
Documents
│
├── report.pdf
│
├── Backup
│   └── report.pdf
│
├── Images
│   └── photo.jpg
│
└── Archive
    └── REPORT.PDF
```

---

## Example Output

```
Duplicate filenames found in the given folder:

report.pdf: 3 occurrences
    D:\Documents\report.pdf
    D:\Documents\Backup\report.pdf
    D:\Documents\Archive\REPORT.PDF

Folders scanned: 4
Files scanned: 4
Duplicate filenames: 1
```

---

## How It Works

1. Recursively walks the selected folder tree using `os.walk()`.
2. Builds a dictionary whose keys are normalized using `str.casefold()`.
3. Stores every full path corresponding to each filename.
4. Reports filenames that occur more than once.
5. Write the result to dup_file_list000.txt file if user confirms it
6. Prints summary statistics.

---

## Limitations

- Duplicate detection is based **only on filenames**.
- File contents are **not** compared.
- File hashes are **not** calculated.
- Hidden files and folders are scanned normally.
- The utility is **read-only** and never modifies files.

---

## Output Statistics

After every scan the utility reports:

- Number of folders scanned
- Number of files scanned
- Number of duplicate filenames found

---

## Future Improvements

Possible future enhancements include:

- Filter by file extension.
- Exclude selected folders.
- Optional graphical interface (Tkinter).
- Progress bar with completion percentage.
- Detect files with identical content, even when their filenames differ.

---

## License

This project is licensed under the MIT License.

---

## Repository

This project is part of the **Automation_Scripts** collection:

https://github.com/aryagohar/Automation_Scripts