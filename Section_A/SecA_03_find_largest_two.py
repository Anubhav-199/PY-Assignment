"""
Section A - Q3: Find Largest of Two Numbers
Concepts: function, return, conditional statement
"""


def find_largest(a, b):
    if a > b:
        return a
    else:
        return b


if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Largest = {find_largest(a, b)}")
