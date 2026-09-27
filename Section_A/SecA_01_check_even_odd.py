"""
Section A - Q1: Even or Odd
Concepts: function, if-else, %
"""


def check_even_odd(n):
    if n % 2 == 0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    check_even_odd(n)
