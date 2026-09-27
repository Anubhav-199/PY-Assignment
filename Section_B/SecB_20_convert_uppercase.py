"""
Section B - Q20: Convert Lowercase to Uppercase
Task: First solve using upper() and then demonstrate a loop-based
solution using character processing.
"""


def convert_uppercase_builtin(text):
    return text.upper()


def convert_uppercase_loop(text):
    result = ""
    for ch in text:
        if "a" <= ch <= "z":
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result


if __name__ == "__main__":
    text = input("Enter a string: ")
    print(f"Uppercase (builtin) : {convert_uppercase_builtin(text)}")
    print(f"Uppercase (loop)    : {convert_uppercase_loop(text)}")
