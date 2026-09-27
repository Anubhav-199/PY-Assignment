"""
Section D - Q30: Number Pattern
Concepts: nested for loops.

For n = 5:
1
12
123
1234
12345
"""


def number_pattern(n):
    for i in range(1, n + 1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)
        print(line)


if __name__ == "__main__":
    n = int(input("Enter n: "))
    number_pattern(n)
