"""
Clipboard-to-list formatter

Reads text from the clipboard, splits it by a selected separator,
numbers each line or prefixes with your own character, and copies the result back to the clipboard.
"""
import pyperclip as pc

RTL_MARK = '\u200f'
LRM_MARK = '\u200e'

def to_persian_digits(value):
    english_digits = "0123456789"
    persian_digits = "۰۱۲۳۴۵۶۷۸۹"
    return str(value).translate(str.maketrans(english_digits, persian_digits))

def has_rtl(text):
    return any('\u0600' <= char <= '\u06FF' for char in text)

def apply_direction(text):
    if has_rtl(text):
        return RTL_MARK + text + RTL_MARK
    return LRM_MARK + text + LRM_MARK

def line_formatter(lines, start_number, flag, full_stop):
    """ Add a number plus a period or only a character to the beginning of each line """
    result_str = ""
    temp = ""
    formatted_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue

        is_rtl = has_rtl(line)
        # direction_mark = RTL_MARK if is_rtl else LRM_MARK
        if flag:
            number = to_persian_digits(start_number) if is_rtl else str(start_number)
            if 10 > start_number >= 0:
                # temp = direction_mark + number + '. ' + line + ('.' if full_stop.lower() == 'y' else '')
                temp = number + '. ' + line + ('.' if full_stop.lower() == 'y' else '')
                temp = apply_direction(temp)
            else:
                # temp = direction_mark + number + '.' + line + ('.' if full_stop.lower() == 'y' else '')
                temp = number + '.' + line + ('.' if full_stop.lower() == 'y' else '')
                temp = apply_direction(temp)
            start_number += 1
        else:
            # temp = direction_mark + start_number + ' ' + line + ('.' if full_stop.lower() == 'y' else '')
            temp = start_number + ' ' + line + ('.' if full_stop.lower() == 'y' else '')
            temp = apply_direction(temp)

        # Append the numbered output to a list
        formatted_lines.append(temp)
        
    # Concatenate list items into a final string
    result_str = '\n'.join(formatted_lines)

    return result_str

def main():
    print('''How is the clipboard text organized? Select an item or input an existing sentence separator:
 1. Each item is in a separate line, new line used as separator
 2. Paragraphs include periods ".", used as separator
 3. Paragraphs include hyphens "-", used as separator
 4. Paragraphs include commas ",", used as separator
 5. Paragraphs include spaces " ", whitespace used as separator
             ''')
    sep_counter = 0
    prefix_counter = 0
    start_number = ''
    separator_choice = ""
    full_stop = ''
    # Input separator and line starting number/line prefix from user
    while True:
        if sep_counter == 0:
            separator_choice = input("Please enter your choice number or an existing string as separator: ")
        if prefix_counter == 0:
            start_number = input("If you want numbered lines: Enter a starting number, "
                                 "Otherwise enter a character or more to prefix to all lines: ")
        full_stop = input("Do you want to end each line of the result with a period? (y/n): ")
        if isinstance(start_number, str) and isinstance(separator_choice, str):
            break
        if isinstance(separator_choice, str):
            sep_counter += 1
        if isinstance(start_number, str):
            prefix_counter += 1
        continue

    # Paste text from clipboard
    text = pc.paste().strip()

    # Check if user pressed Enter instead of a separator
    if separator_choice == '':
        if '\n' in text:
            separator_choice = '\n'
        else:
            separator_choice = '.'

    # Check if user pressed Enter instead of a valid prefix
    if start_number == '':
       start_number = '1'

    # split lines in the text into a list through separator
    split_dict = {
        '1': '\n',
        '2': '.',
        '3': '-',
        '4': ',',
        '5': None,
    }
    separator = split_dict.get(separator_choice, separator_choice)
    lines = text.split(separator)

    # Remove probable empty members in the list
    for item in lines.copy():
        if item.strip() == '':
            lines.remove(item)

    flag = True
    try:
        start_number = int(start_number)
    except ValueError:
        flag = False
    # Create and copy the formatted output back to clipboard
    pc.copy(line_formatter(lines, start_number, flag, full_stop))
    print("\nNumbered text copied to clipboard.")

if __name__ == '__main__':
    main()
