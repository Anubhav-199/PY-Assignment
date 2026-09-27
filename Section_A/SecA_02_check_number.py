"""
Section A - Q2: Positive, Negative or Zero
Concepts: function, if-elif-else
"""


def check_number(n):
    if n > 0:
        print(f"{n} is Positive")
    elif n < 0:
        print(f"{n} is Negative")
    else:
        print(f"{n} is Zero")


if __name__ == "__main__":
    n = float(input("Enter a number: "))
    check_number(n)
