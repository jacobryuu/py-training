def solution(n: int) -> int:
    """Find the longest binary gap in a number"""
    if n < 5:
        return 0
    
    binary_str = bin(n)[2:]  # Remove '0b' prefix
    sub_str = binary_str[1:]
    
    if '1' not in sub_str:
        return 0
    
    # Find the substring between first and last '1' after the first bit
    last_one_idx = sub_str.rfind('1')
    if last_one_idx < 0:
        return 0
    
    sub_length = sub_str[:last_one_idx].split('1')
    if len(sub_length) == 0:
        return 0
    
    return max(len(s) for s in sub_length)


def binary_gap_count(n: int) -> int:
    """Count binary gap using bit manipulation"""
    max_gap = 0
    current_gap = 0
    counting = False
    
    while n > 0:
        if (n & 1) == 1:  # Check if least significant bit is 1
            if counting:
                max_gap = max(max_gap, current_gap)
            counting = True
            current_gap = 0
        elif counting:
            current_gap += 1
        n >>= 1  # Right shift
    
    return max_gap


def main():
    n = 1041
    print(f"result: {solution(n)}")
    num = 1041
    print(f"result: {binary_gap_count(num)}")


if __name__ == "__main__":
    main()
