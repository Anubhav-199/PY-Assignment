"""
Section B - Q17: Count Words
Restriction: Do not use split().
Hint: Count spaces carefully.

Example:
Input : Python is easy to learn
Output : 5
"""


def count_words(text):
    if text == "":
        return 0
    word_count = 1
    for ch in text:
        if ch == " ":
            word_count += 1
    return word_count


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print(f"Number of words = {count_words(text)}")
