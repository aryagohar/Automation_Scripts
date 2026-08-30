# Smart Batch PDF Cipher

[![Python Version](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)

[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)]()

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)

[![Status](https://img.shields.io/badge/Status-Active-success)]()

[![AES-256](https://img.shields.io/badge/Encryption-AES--256-blue)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)

[![pypdf](https://img.shields.io/badge/PDF-pypdf-red)](https://pypi.org/project/pypdf/)

[![Cryptography](https://img.shields.io/badge/Cryptography-AES--256-orange)](https://pypi.org/project/cryptography/)

[![GitHub release](https://img.shields.io/github/v/release/aryagohar/Automation_Scripts)](https://github.com/aryagohar/Automation_Scripts/releases)

[![Downloads](https://img.shields.io/github/downloads/aryagohar/Automation_Scripts/total)](https://github.com/aryagohar/Automation_Scripts/releases)

[![Repo Size](https://img.shields.io/github/repo-size/aryagohar/Automation_Scripts)](https://github.com/aryagohar/Automation_Scripts)

[![Last Commit](https://img.shields.io/github/last-commit/aryagohar/Automation_Scripts)](https://github.com/aryagohar/Automation_Scripts)

[![Stars](https://img.shields.io/github/stars/aryagohar/Automation_Scripts?style=social)](https://github.com/aryagohar/Automation_Scripts)


A lightweight Python command-line utility for **batch encrypting and decrypting PDF files recursively**.

**Smart Batch PDF Cipher** uses [`pypdf`](https://pypi.org/project/pypdf/) together with [`cryptography`](https://pypi.org/project/cryptography/) to encrypt PDF files using **AES-256**.

The program recursively scans a target directory and its subdirectories, creates encrypted or decrypted copies, verifies successful processing, and then removes the original file.

> ⚠️ **Important:** The program deletes the original PDF after successful processing. Always make a backup of important documents before using this tool.

---

## Features

- 🔐 Batch encrypt PDF files using **AES-256**
- 🔓 Batch decrypt password-protected PDF files
- 📁 Recursively process all subdirectories
- 💻 Command-line interface using Python `argparse`
- 🔑 Secure interactive password input using Python `getpass`
- 🚫 Password is **not displayed while typing**
- ⚡ Supports full commands and short aliases
- 🛡️ Verifies encrypted files before deleting originals
- 🔢 Displays the number of successfully processed files
- 🚫 Skips files already ending with `_encrypted.pdf` during encryption
- 📂 Preserves the existing directory structure
- 🐍 Can be used directly as a Python script
- 🪟 A ready-to-use Windows executable is also provided
- 🚫 Does not require Adobe Acrobat or other PDF software

---

# Requirements

## Python Version

- Python **3.8+**

## Required Python Libraries

The script requires:

- `pypdf`
- `cryptography`

`cryptography` is required by the PDF encryption implementation for **AES-256** support.

The program is designed to work on:

- Windows
- Linux
- macOS

---

# Installation

## Option 1 — Run the Python Script

### 1. Check Python

Verify that Python is installed:

```bash
python --version
```

or:

```bash
python3 --version
```

### 2. Install Required Libraries

Install both required packages:

```bash
pip install pypdf cryptography
```

Or, on systems using `python3`:

```bash
python3 -m pip install pypdf cryptography
```

### 3. Download the Script

The Python script is named:

```text
smart_batch_pdf_cipher.py
```

A typical project structure is:

```text
Smart-Batch-PDF-Cipher/
│
├── smart_batch_pdf_cipher.py
├── README.md
└── LICENSE
```

---

# Option 2 — Use the Windows Executable

A ready-to-use Windows executable is also available:

```text
smart_batch_pdf_cipher.exe
```

The executable does **not require you to install Python or the Python libraries separately**.

Place the executable in a convenient location and run it from Command Prompt, PowerShell, or a terminal.

Example:

```powershell
smart_batch_pdf_cipher.exe encrypt --path "C:\Documents\PDFs"
```

The program will then securely prompt you for the password.

---

# Usage

The general syntax for the Python script is:

```bash
python smart_batch_pdf_cipher.py MODE --path DIRECTORY
```

For the executable:

```powershell
smart_batch_pdf_cipher.exe MODE --path DIRECTORY
```

Where:

| Argument | Description |
|---|---|
| `MODE` | `encrypt`, `en`, `decrypt`, or `de` |
| `--path` | Target directory; defaults to the current directory |

> **Note:** The password is **not supplied on the command line**. The program securely prompts for it after validating the command-line arguments and target directory.

---

# Encrypt PDF Files

To encrypt PDFs in a directory:

```bash
python smart_batch_pdf_cipher.py encrypt --path "C:\Documents\PDFs"
```

Or using the short alias:

```bash
python smart_batch_pdf_cipher.py en --path "C:\Documents\PDFs"
```

The program will prompt:

```text
Enter password for PDF operations:
```

The password will not be displayed while you type.

---

## Using the Executable

```powershell
smart_batch_pdf_cipher.exe encrypt --path "C:\Documents\PDFs"
```

or:

```powershell
smart_batch_pdf_cipher.exe en --path "C:\Documents\PDFs"
```

---

## Encryption Example

Suppose the target directory contains:

```text
Documents/
├── report.pdf
├── invoice.pdf
└── Projects/
    ├── project1.pdf
    └── project2.pdf
```

After successful encryption:

```text
Documents/
├── report_encrypted.pdf
├── invoice_encrypted.pdf
└── Projects/
    ├── project1_encrypted.pdf
    └── project2_encrypted.pdf
```

The original PDFs are deleted **only after the encrypted files have been successfully created and verified**.

---

# Decrypt PDF Files

To decrypt PDFs:

```bash
python smart_batch_pdf_cipher.py decrypt --path "C:\Documents\PDFs"
```

Or using the short alias:

```bash
python smart_batch_pdf_cipher.py de --path "C:\Documents\PDFs"
```

The program will prompt you for the password.

---

## Using the Executable

```powershell
smart_batch_pdf_cipher.exe decrypt --path "C:\Documents\PDFs"
```

or:

```powershell
smart_batch_pdf_cipher.exe de --path "C:\Documents\PDFs"
```

---

## Decryption Example

Suppose the directory contains:

```text
Documents/
├── report_encrypted.pdf
└── Projects/
    └── project1_encrypted.pdf
```

After successful decryption:

```text
Documents/
├── report_encrypted_decrypted.pdf
└── Projects/
    └── project1_encrypted_decrypted.pdf
```

The encrypted source files are removed after successful decryption.

---

# Using the Current Directory

If `--path` is omitted, the program processes the **current working directory**.

For example:

```bash
python smart_batch_pdf_cipher.py encrypt
```

is equivalent to:

```bash
python smart_batch_pdf_cipher.py encrypt --path "."
```

For the executable:

```powershell
smart_batch_pdf_cipher.exe encrypt
```

This recursively processes PDF files in the current directory and all its subdirectories.

---

# Password Security

One important improvement in the current version is that the password is **not passed as a command-line argument**.

The program uses Python's `getpass` module:

```python
from getpass import getpass
```

and prompts for the password only after:

1. Command-line arguments have been parsed.
2. The target directory has been resolved.
3. The target directory has been validated.

The password is entered through:

```python
password = getpass("Enter password for PDF operations: ")
```

This prevents the password from being displayed on the terminal while it is being entered.

It also avoids exposing the password directly through the command line, shell history, or process arguments.

---

# Empty Password Protection

The program does not allow an empty password.

If the user presses Enter without entering a password, the program displays:

```text
Error: Password cannot be empty.
```

and exits without processing any files.

---

# Encryption

PDF encryption is performed with:

```python
writer.encrypt(password, algorithm="AES-256")
```

The encryption process uses **AES-256** through `pypdf` and its cryptographic dependency.

The workflow is:

1. Find a PDF file.
2. Create a `PdfWriter`.
3. Append the original PDF.
4. Encrypt it using AES-256.
5. Save it as `*_encrypted.pdf`.
6. Re-open the newly created file.
7. Test the supplied password.
8. Delete the original PDF only if verification succeeds.

---

# Decryption

During decryption, the program first checks:

```python
reader.is_encrypted
```

If the PDF is encrypted, the supplied password is tested.

If the password is correct:

1. The PDF is opened.
2. A new PDF is created.
3. The decrypted contents are written to the new file.
4. The encrypted source file is deleted.

If the password is incorrect, the original encrypted PDF remains untouched.

---

# File Naming Convention

The program does not directly overwrite the original PDF.

## Encryption

```text
document.pdf
```

becomes:

```text
document_encrypted.pdf
```

## Decryption

For example:

```text
document_encrypted.pdf
```

becomes:

```text
document_encrypted_decrypted.pdf
```

The program uses the original filename's stem:

```python
full_file_path.stem
```

to construct the new filename.

---

# Recursive Processing

The program uses Python's `os.walk()`:

```python
for folder_name, _, filenames in os.walk(target_dir):
```

Therefore, it processes PDF files at any depth below the target directory.

For example:

```text
PDFs/
├── document1.pdf
│
├── Work/
│   ├── report.pdf
│   │
│   └── Projects/
│       ├── project.pdf
│       └── Archive/
│           └── old_project.pdf
│
└── Personal/
    └── personal.pdf
```

Running the program against `PDFs/` recursively processes all matching PDFs.

The existing directory structure is preserved.

---

# Command-Line Options

Display the built-in help with:

```bash
python smart_batch_pdf_cipher.py --help
```

For the executable:

```powershell
smart_batch_pdf_cipher.exe --help
```

The available commands are:

| Option | Description |
|---|---|
| `encrypt` | Encrypt PDF files |
| `en` | Short alias for `encrypt` |
| `decrypt` | Decrypt PDF files |
| `de` | Short alias for `decrypt` |
| `--path PATH` | Target directory |
| `-h`, `--help` | Display help |

---

# Examples

## Encrypt a Folder

```bash
python smart_batch_pdf_cipher.py encrypt --path "D:\My Documents"
```

---

## Encrypt Using the Short Alias

```bash
python smart_batch_pdf_cipher.py en --path "D:\My Documents"
```

---

## Decrypt a Folder

```bash
python smart_batch_pdf_cipher.py decrypt --path "D:\My Documents"
```

---

## Decrypt Using the Short Alias

```bash
python smart_batch_pdf_cipher.py de --path "D:\My Documents"
```

---

## Process the Current Directory

```bash
python smart_batch_pdf_cipher.py encrypt
```

---

## Using the Executable

Encrypt:

```powershell
smart_batch_pdf_cipher.exe encrypt --path "D:\My Documents"
```

Decrypt:

```powershell
smart_batch_pdf_cipher.exe decrypt --path "D:\My Documents"
```

Current directory:

```powershell
smart_batch_pdf_cipher.exe encrypt
```

---

# Example Session

```text
C:\PDFs> smart_batch_pdf_cipher.exe encrypt --path "D:\Documents"

Enter password for PDF operations:
Done: 8 PDF(s) encrypted.
```

For an incorrect password during decryption:

```text
Enter password for PDF operations:
Incorrect password for report_encrypted.pdf!
Done: 0 PDF(s) decrypted.
```

---

# How It Works

## Encryption Workflow

```text
Start
  │
  ▼
Parse command-line arguments
  │
  ▼
Resolve target directory
  │
  ▼
Validate directory
  │
  ▼
Prompt for password
  │
  ▼
Validate password
  │
  ▼
Recursively scan directories
  │
  ▼
Find PDF files
  │
  ▼
Create encrypted PDF
  │
  ▼
Save as *_encrypted.pdf
  │
  ▼
Verify encrypted file
  │
  ├── Success ──► Delete original PDF
  │
  └── Failure ──► Keep original PDF
  │
  ▼
Continue
```

## Decryption Workflow

```text
Start
  │
  ▼
Parse command-line arguments
  │
  ▼
Resolve target directory
  │
  ▼
Validate directory
  │
  ▼
Prompt for password
  │
  ▼
Validate password
  │
  ▼
Recursively scan directories
  │
  ▼
Find PDF files
  │
  ▼
Check encryption status
  │
  ├── Not encrypted ──► Skip
  │
  └── Encrypted
        │
        ▼
   Test password
        │
        ├── Incorrect ──► Keep original
        │
        └── Correct
              │
              ▼
       Create decrypted PDF
              │
              ▼
       Delete encrypted PDF
              │
              ▼
           Continue
```

---

# Technical Details

## Python Standard Library

The script uses:

```python
import argparse
import logging
import os
import sys
from pathlib import Path
from getpass import getpass
```

| Module | Purpose |
|---|---|
| `argparse` | Command-line argument parsing |
| `logging` | Suppressing unnecessary `pypdf` warnings |
| `os` | Recursive directory traversal and file deletion |
| `sys` | Exiting with an error status |
| `pathlib` | Cross-platform filesystem path handling |
| `getpass` | Secure password input |

## External Libraries

```python
import pypdf
```

| Package | Purpose |
|---|---|
| `pypdf` | Reading, writing, encrypting, and decrypting PDFs |
| `cryptography` | Cryptographic support required for AES-256 encryption |

Install both with:

```bash
pip install pypdf cryptography
```

---

# Project Structure

A recommended repository structure is:

```text
Smart-Batch-PDF-Cipher/
│
├── smart_batch_pdf_cipher.py
├── smart_batch_pdf_cipher.exe
├── README.md
└── LICENSE
```

The executable can be placed in the GitHub repository's **Releases** section rather than directly in the repository if the file is large.

---

# Important Safety Considerations

## ⚠️ Original Files Are Deleted

This is the most important behavior to understand.

During encryption:

```python
os.remove(full_file_path)
```

removes the original PDF after successful verification.

During decryption:

```python
os.remove(full_file_path)
```

removes the encrypted PDF after successful decryption.

Therefore:

> **Never use this program on your only copy of important documents.**

A recommended workflow is:

```text
Original PDFs
      │
      ├──► Backup
      │
      └──► Test with copies
               │
               ▼
       Run Smart Batch PDF Cipher
```

---

## Password Loss

The program does not provide password recovery.

If you encrypt a PDF and subsequently forget the password, the encrypted PDF may be inaccessible.

**Keep your passwords safe.**

---

# Error Handling

The program catches exceptions while processing individual PDF files.

For encryption:

```python
except Exception as e:
    print(f"Error encrypting {filename}: {e}")
```

For decryption:

```python
except Exception as e:
    print(f"Error decrypting {filename}: {e}")
```

Possible causes of errors include:

- Corrupted PDF files
- Unsupported PDF structures
- Incorrect passwords
- Permission problems
- Files locked by another application
- Insufficient disk space
- Inaccessible directories
- Filesystem errors

An error affecting one PDF does not necessarily stop processing of the remaining files.

---

# Current Limitations

The current version intentionally keeps the interface simple.

Current limitations include:

- There is no `--dry-run` mode.
- There is no interactive confirmation before deleting originals.
- There is no option to specify a separate output directory.
- There is no progress bar.
- There is no detailed log file.
- Existing `_decrypted.pdf` files are not explicitly excluded during decryption.
- The program processes PDFs recursively from the specified directory.
- The original file is removed after successful processing.


# Possible Future Improvements

Potential future enhancements include:

- [ ] `--dry-run` mode
- [ ] Optional preservation of original files
- [ ] Confirmation before deleting originals
- [ ] Progress bar
- [ ] Detailed logging
- [ ] Log file generation
- [ ] Output directory option
- [ ] File filtering options
- [ ] Folder exclusion options
- [ ] Better exit codes for automation
- [ ] Password confirmation during encryption
- [ ] Password strength validation
- [ ] Unit tests
- [ ] Automated CI testing
- [ ] Additional PDF encryption options
- [ ] Linux and macOS executable releases

---

# License

This project is released under the **MIT License**.

You are free to use, modify, distribute, and include this software in other projects, subject to the terms of the license.

See [`LICENSE`](LICENSE) for the complete license text.

---

# Disclaimer

This software is provided **"as-is"**, without warranty of any kind.

The author is not responsible for:

- Data loss
- Corrupted PDF files
- Lost or forgotten passwords
- Incorrect password usage
- Files deleted by the program
- Damage resulting from improper use

**Always maintain a backup of important documents before using this software.**

---

# Author

Developed as a Python automation utility for **batch PDF encryption and decryption**.

If you find this project useful, consider ⭐ starring the repository on GitHub.

---

# Quick Reference

### Python — Encrypt

```bash
python smart_batch_pdf_cipher.py encrypt --path "DIRECTORY"
```

### Python — Encrypt (short alias)

```bash
python smart_batch_pdf_cipher.py en --path "DIRECTORY"
```

### Python — Decrypt

```bash
python smart_batch_pdf_cipher.py decrypt --path "DIRECTORY"
```

### Python — Decrypt (short alias)

```bash
python smart_batch_pdf_cipher.py de --path "DIRECTORY"
```

### Executable — Encrypt

```powershell
smart_batch_pdf_cipher.exe encrypt --path "DIRECTORY"
```

### Executable — Decrypt

```powershell
smart_batch_pdf_cipher.exe decrypt --path "DIRECTORY"
```

### Current Directory

```bash
python smart_batch_pdf_cipher.py encrypt
```

or:

```powershell
smart_batch_pdf_cipher.exe encrypt
```

### Help

```bash
python smart_batch_pdf_cipher.py --help
```

or:

```powershell
smart_batch_pdf_cipher.exe --help
```

---

## 🔐 Security Reminder

**Smart Batch PDF Cipher uses AES-256 PDF encryption and does not expose the password while it is being entered.**

**Always keep a backup of your original PDFs and securely store your passwords.**
