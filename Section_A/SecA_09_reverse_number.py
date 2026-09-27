"""
Section A - Q9: Reverse a Number
Concepts: while, %, //

Example:
Input : 12345
Output : 54321
"""


def reverse_number(n):
    negative = n < 0
    n = abs(n)
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return -reversed_num if negative else reversed_num


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Reversed number = {reverse_number(n)}")
