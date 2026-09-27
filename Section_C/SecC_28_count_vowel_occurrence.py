"""
Section C - Q28: Count Occurrence of Each Vowel
Restriction: Use loops and conditions.

Example:
Input: education
Output:
a = 1
e = 1
i = 1
o = 1
u = 1
"""


def count_vowel_occurrences(text):
    a = e = i = o = u = 0
    for ch in text.lower():
        if ch == "a":
            a += 1
        elif ch == "e":
            e += 1
        elif ch == "i":
            i += 1
        elif ch == "o":
            o += 1
        elif ch == "u":
            u += 1
    print(f"a = {a}")
    print(f"e = {e}")
    print(f"i = {i}")
    print(f"o = {o}")
    print(f"u = {u}")


if __name__ == "__main__":
    text = input("Enter a string: ")
    count_vowel_occurrences(text)
