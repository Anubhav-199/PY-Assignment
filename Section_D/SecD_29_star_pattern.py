"""
Section D - Q29: Star Pattern
Concepts: nested loops.

For n = 5:
*
**
***
****
*****
"""


def star_pattern(n):
    for i in range(1, n + 1):
        print("*" * i)


if __name__ == "__main__":
    n = int(input("Enter n: "))
    star_pattern(n)
