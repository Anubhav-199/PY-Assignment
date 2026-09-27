"""
Section A - Q4: Find Largest of Three Numbers
Restriction: Do not use max().
"""


def find_largest(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest


if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    print(f"Largest = {find_largest(a, b, c)}")
