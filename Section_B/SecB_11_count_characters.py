"""
Section B - Q11: Count Characters in a String
Restriction: Do not use len().
Concepts: for loop, counter
"""


def count_characters(text):
    count = 0
    for ch in text:
        count += 1
    return count


if __name__ == "__main__":
    text = input("Enter a string: ")
    print(f"Number of characters = {count_characters(text)}")
