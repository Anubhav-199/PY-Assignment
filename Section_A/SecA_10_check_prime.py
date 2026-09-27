"""
Section A - Q10: Prime Number
Restriction: Use a loop and do not use any external library.
"""


def check_prime(n):
    if n < 2:
        print(f"{n} is not a Prime number")
        return
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n} is a Prime number")
    else:
        print(f"{n} is not a Prime number")


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    check_prime(n)
