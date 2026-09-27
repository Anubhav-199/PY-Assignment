"""
Section B - Q12: Count Vowels
Restriction: Use a loop.

Example:
Input : education
Output : 5
"""


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


if __name__ == "__main__":
    text = input("Enter a string: ")
    print(f"Number of vowels = {count_vowels(text)}")
