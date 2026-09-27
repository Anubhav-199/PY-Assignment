"""
Section A - Q8: Count Digits
Restriction: Use a while loop.
"""


def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Number of digits = {count_digits(n)}")
