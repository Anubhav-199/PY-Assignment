"""
Section C - Q26: Remove Vowels
Restriction: Use a loop. Do not use replace().

Example:
Input: Python Programming
Output: Pythn Prgrmmng
"""


def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch
    return result


if __name__ == "__main__":
    text = input("Enter a string: ")
    print(f"Without vowels = {remove_vowels(text)}")
