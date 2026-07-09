# Smart Clipboard List Formatter

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

A lightweight yet powerful Python utility that transforms clipboard text into clean, well-formatted lists.
The program reads text directly from your clipboard, splits it using a predefined or custom separator, formats each item as either a numbered or prefixed list, intelligently detects right-to-left (RTL) languages such as Persian and Arabic, applies the correct writing direction, and copies the final result back to the clipboard.
It is especially useful for quickly converting copied text into lists for documentation, Markdown files, Word documents, presentations, emails, note-taking applications, and AI prompts.
________________________________________
## Quick Start
### Option 1: Download the Executable
This .exe file was built from the source code.
If you don't have Python installed, download the latest standalone Windows executable from the **Releases** page.
1. Open the **Releases** page.
2. Download ` Smart Clipboard List Formatter.exe`.
3. Run the executable.
No installation or Python environment is required.
-----------------------
### Option 2: Run from Source
Clone the repository and install the required dependency:
```bash 
pip install pyperclip
python Smart Clipboard List Formatter.py
```
________________________________________
## Features
- Standalone Windows executable (.exe) available in the Releases section.
  
**Clipboard Integration**
- Reads input directly from the system clipboard.
- Automatically copies the formatted result back to the clipboard.
- No intermediate files required.
________________________________________
**Flexible Text Splitting**
Supports the following separators:
- New lines
- Periods (.)
- Hyphens (-)
- Commas (,)
- Spaces (any whitespace)
- Any custom separator string entered by the user.
If no separator is entered:
- New lines are used when present.
- Otherwise periods (.) are used automatically.
________________________________________
**Multiple List Styles**
Generate:
- Numbered lists
- Bulleted lists
- Custom prefixes
- Markdown lists
- Checklist prefixes
- Quoted text
Examples of custom prefixes: - * > • ✓ → ■
________________________________________
### Intelligent RTL Language Support
One of the major features of this utility is automatic handling of right-to-left languages.
Supported examples include:
- Persian (Farsi)
- Arabic
**Features include:**
- Automatic RTL detection
- Automatic insertion of Unicode direction marks
- Correct display when pasted into Microsoft Word
- Correct display in Markdown editors
- Correct display in browsers
- Correct display in most modern text editors
  Mixed Persian and English content is handled correctly.
________________________________________
**Automatic Number Localization**
When numbered output is selected:
- English text receives English digits.
 Example:
1. Apple
2. Orange
3. Banana
- Persian/Arabic text automatically receives Persian digits.
  Example:
  
۱. سیب
۲. پرتقال
۳. موز

No configuration is required.
________________________________________
**Optional Ending Period**
The program can automatically append a period to every generated line.
Example without period:
1. Apple
2. Orange
3. Banana
   
Example with period:
1. Apple is a fruit.
2. I like travelling.
3. He is my best friend.
________________________________________
**Automatic Cleanup**
The formatter automatically:
- Removes empty items
- Trims leading spaces
- Trims trailing spaces
- Ignores blank lines
________________________________________
**Requirements**
- Python 3.8 or newer
  
**Dependency**
```bash 
pip install pyperclip
```
________________________________________
**Installation**
Clone the repository:
```bash 
git clone https://github.com/aryagohar/ Automation_Scripts.git
```
Move into the project directory:
```bash 
cd <repository>
```
Install the dependency:
```bash 
pip install pyperclip
```
Run:
```bash 
python Smart Clipboard List Formatter.py
```
________________________________________
**Usage**
Step 1
Copy some text to your clipboard.
________________________________________
Step 2
Run the program.
________________________________________
Step 3
Choose how the clipboard text is separated.
```text
1. New line
2. Period
3. Hyphen
4. Comma
5. Space
```
You may also type your own custom separator.
________________________________________
Step 4
Choose how each line should begin.
Either

-Enter a starting number
Example:
1
or

-Enter any custom prefix
Examples: - * > • ✓

- Pressing Enter starts numbering from 1.
________________________________________
Step 5
Choose whether each generated line should end with a period.
Do you want to end each line of the result with a period? (y/n)
________________________________________
Step 6
The formatted result is automatically copied back to the clipboard.
Simply paste it wherever you need.
________________________________________
Examples
Example 1 – Numbered English List

Clipboard:
Apple, Orange, Banana, Mango

Select Separator: ,
Starting number: 1

Output:

```text
1. Apple
2. Orange
3. Banana
4. Mango
```
________________________________________
Example 2 – Markdown Bullet List
Clipboard:
Python
Java
Rust
Go

Prefix: -

Output:

```text
- Python
- Java
- Rust
- Go
```
________________________________________
Example 3 – Persian Numbering

Clipboard:
سیب، پرتقال، موز

Output:

۱. سیب
۲. پرتقال
۳. موز


No configuration is required.

The program automatically detects RTL text and switches to Persian digits.
________________________________________
Example 4 – Custom Prefix

Clipboard:

Install Python
Install Git
Create Repository

Prefix:  ✓

Output:

```text
✓ Install Python
✓ Install Git
✓ Create Repository
```
________________________________________
**Supported Separators**
User Input	Separator
1	New line (\n)
2	Period (.)
3	Hyphen (-)
4	Comma (,)
5	space(Whitespace)
Any other text	Custom separator
________________________________________
### Typical Use Cases
- Formatting copied web content
- Creating numbered documentation
- Preparing Markdown lists
- Organizing research notes
- Formatting AI prompts
- Preparing Microsoft Word documents
- Creating PowerPoint bullet lists
- Converting copied paragraphs into lists
- Cleaning clipboard text before pasting
- Formatting Persian and English mixed documents
________________________________________
**Project Structure**
Smart Clipboard List Formatter.py
Main components:
- Clipboard handling
- Text splitting
- List formatting
- RTL detection
- Unicode direction management
- Persian digit conversion
________________________________________
**License**
This project is licensed under the MIT License.
________________________________________
**Acknowledgements**
This project uses the excellent pyperclip library for cross-platform clipboard access.
Special attention has been given to proper handling of right-to-left languages and Unicode text direction to ensure reliable results across modern editors and applications.
