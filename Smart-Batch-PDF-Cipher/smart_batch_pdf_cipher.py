import argparse
import logging
import os
import sys
from pathlib import Path
import pypdf
from getpass import getpass

# Suppress pypdf internal warnings in the console
logging.getLogger("pypdf").setLevel(logging.ERROR)


def encrypt_pdfs(target_dir: Path, password: str) -> None:
    counter = 0
    for folder_name, _, filenames in os.walk(target_dir):
        for filename in filenames:
            if filename.lower().endswith(".pdf") and not filename.endswith("_encrypted.pdf"):
                full_file_path = Path(folder_name) / filename
                writer = pypdf.PdfWriter()
                try:
                    writer.append(full_file_path)
                    writer.encrypt(password, algorithm="AES-256")

                    new_filename = f"{full_file_path.stem}_encrypted.pdf"
                    new_file_path = Path(folder_name) / new_filename

                    with open(new_file_path, "wb") as f:
                        writer.write(f)
                        counter += 1

                    # Verify encrypted file
                    reader = pypdf.PdfReader(new_file_path)
                    if reader.decrypt(password).name != "NOT_DECRYPTED":
                        os.remove(full_file_path)
                    else:
                        print(f"Decryption test failed for {filename}!")
                except Exception as e:
                    print(f"Error encrypting {filename}: {e}")

    print(f"Done: {counter} PDF(s) encrypted.")


def decrypt_pdfs(target_dir: Path, password: str) -> None:
    counter = 0
    for folder_name, _, filenames in os.walk(target_dir):
        for filename in filenames:
            if filename.lower().endswith(".pdf"):
                full_file_path = Path(folder_name) / filename
                try:
                    reader = pypdf.PdfReader(full_file_path)
                    if reader.is_encrypted:
                        writer = pypdf.PdfWriter()
                        new_filename = f"{full_file_path.stem}_decrypted.pdf"
                        new_file_path = Path(folder_name) / new_filename

                        if reader.decrypt(password).name != "NOT_DECRYPTED":
                            writer.append(reader)
                            with open(new_file_path, "wb") as f:
                                writer.write(f)
                                counter += 1
                            os.remove(full_file_path)
                        else:
                            print(f"Incorrect password for {filename}!")
                except Exception as e:
                    print(f"Error decrypting {filename}: {e}")

    print(f"Done: {counter} PDF(s) decrypted.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Batch encrypt or decrypt PDF files recursively."
    )
    # Accept both full terms and short aliases
    parser.add_argument(
        "mode",
        choices=["encrypt", "en", "decrypt", "de"],
        help="Action to perform: 'encrypt' / 'en' or 'decrypt' / 'de'",
    )
    parser.add_argument(
        "--path",
        default=".",
        help="Target directory path (defaults to current directory)",
    )

    # 1. Parse arguments first
    args = parser.parse_args()
    target = Path(args.path).resolve()

    # 2. Validate directory existence
    if not target.exists():
        print(f"Error: Directory '{target}' does not exist.")
        sys.exit(1)

    # 3. Prompt for password ONLY after arguments and paths pass validation
    password = getpass("Enter password for PDF operations: ")

    if not password:
        print("Error: Password cannot be empty.")
        sys.exit(1)

    # 4. Route aliases to their respective functions
    if args.mode in ["encrypt", "en"]:
        encrypt_pdfs(target, password)
    elif args.mode in ["decrypt", "de"]:
        decrypt_pdfs(target, password)