def count_ones(binary: str) -> int:
    """Count the number of 1's in a binary string"""
    count = 0
    for c in binary:
        if c == '1':
            count += 1
    return count


def count_ones1(binary: str) -> int:
    """Count the number of 1's in a binary string (alternative)"""
    count = 0
    length = len(binary)
    for i in range(length):
        if binary[i] == '1':
            count += 1
    return count


def main():
    binary = "1101010111"
    ones_count = count_ones1(binary)
    print(f"Number of 1's in {binary}: {ones_count}")
    
    # Using built-in method
    print(f"Number of 1's count: {bin(int(binary, 2)).count('1')}")


if __name__ == "__main__":
    main()
