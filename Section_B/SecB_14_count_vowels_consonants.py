"""
Section B - Q14: Count Vowels and Consonants
Example:
Input : Python Programming
Vowels : 4
Consonants : 14
"""


def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    print(f"Vowels : {vowel_count}")
    print(f"Consonants : {consonant_count}")


if __name__ == "__main__":
    text = input("Enter a string: ")
    count_vowels_consonants(text)
