def is_happy(n: int) -> bool:
    """Check if a number is a happy number"""
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = next_number(n)
    return n == 1


def next_number(n: int) -> int:
    """Calculate sum of squares of digits"""
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total


def main():
    num = 10
    print(f"{num} is happy? {is_happy(num)}")


if __name__ == "__main__":
    main()
