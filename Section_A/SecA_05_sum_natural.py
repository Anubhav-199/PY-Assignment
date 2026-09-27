"""
Section A - Q5: Sum of Natural Numbers
Restriction: Use a for loop.

Example:
Enter n: 10
Sum = 55
"""


def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(f"Sum = {sum_natural(n)}")
