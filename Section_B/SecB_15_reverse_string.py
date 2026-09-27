"""
Section B - Q15: Reverse a String
Restriction: Demonstrate both approaches.
Approach 1: Using a loop
Approach 2: Using string slicing text[::-1]
"""


def reverse_string_loop(text):
    reversed_text = ""
    for ch in text:
        reversed_text = ch + reversed_text
    return reversed_text


def reverse_string_slicing(text):
    return text[::-1]


if __name__ == "__main__":
    text = input("Enter a string: ")
    print(f"Reversed (loop)    : {reverse_string_loop(text)}")
    print(f"Reversed (slicing) : {reverse_string_slicing(text)}")
