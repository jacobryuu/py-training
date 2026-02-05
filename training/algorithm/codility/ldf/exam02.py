def solution(S: str) -> str:
    """Add thousand separators to number string"""
    s = S
    offset = len(S)
    
    if '.' in s:
        offset = s.index('.')
        s = s[:s.index('.')]
    
    step = 3
    if '-' in s:
        length = len(s) - 1
    else:
        length = len(s)
    
    num = length // step
    result = list(S)
    
    for i in range(num):
        offset = offset - 3
        result.insert(offset, ',')
    
    return ''.join(result)


def solution2(S: str) -> str:
    """Add thousand separators to number string (alternative)"""
    if not S:
        return S
    
    is_negative = S.startswith('-')
    start_idx = 1 if is_negative else 0
    
    dot_index = S.find('.')
    integer_part = S[start_idx:] if dot_index == -1 else S[start_idx:dot_index]
    decimal_part = '' if dot_index == -1 else S[dot_index:]
    
    result = []
    count = 0
    
    for i in range(len(integer_part) - 1, -1, -1):
        result.append(integer_part[i])
        count += 1
        if count % 3 == 0 and i > 0:
            result.append(',')
    
    result.reverse()
    
    if is_negative:
        result.insert(0, '-')
    
    return ''.join(result) + decimal_part


def main():
    print(solution("1234567"))  # 1,234,567
    print(solution("-1234567"))  # -1,234,567
    print(solution("1234567.89"))  # 1,234,567.89
    print(solution("-1234.567"))  # -1,234.567
    print(solution("100"))  # 100
    print(solution("-1000"))  # -1,000
    print(solution("0"))  # 0
    print("--------")
    print(solution2("1234567"))  # 1,234,567
    print(solution2("-1234567"))  # -1,234,567
    print(solution2("1234567.89"))  # 1,234,567.89
    print(solution2("-1234.567"))  # -1,234.567
    print(solution2("100"))  # 100
    print(solution2("-1000"))  # -1,000
    print(solution2("0"))  # 0


if __name__ == "__main__":
    main()
