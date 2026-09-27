"""
Section B - Q19: Remove Spaces
Restriction: Use a loop.

Example:
Input : Python Programming Language
Output : PythonProgrammingLanguage
"""


def remove_spaces(text):
    result = ""
    for ch in text:
        if ch != " ":
            result += ch
    return result


if __name__ == "__main__":
    text = input("Enter a string: ")
    print(f"Without spaces = {remove_spaces(text)}")
