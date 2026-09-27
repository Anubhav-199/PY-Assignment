"""
Section B - Q13: Count Consonants
Assume: Input contains alphabetic characters and spaces.
"""


def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count


if __name__ == "__main__":
    text = input("Enter a string: ")
    print(f"Number of consonants = {count_consonants(text)}")
