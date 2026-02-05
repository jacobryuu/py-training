from collections import Counter


def solution(s: str) -> int:
    """Count characters that appear exactly once"""
    result = 0
    for ch in s:
        if s.index(ch) == s.rindex(ch):
            result += 1
    return result


def solution2(s: str) -> int:
    """Count characters that appear exactly once using Counter"""
    char_count = Counter(s)
    return sum(1 for count in char_count.values() if count == 1)


def count_unique_characters(s: str) -> int:
    """Count characters that appear exactly once"""
    frequency_map = {}
    for ch in s:
        frequency_map[ch] = frequency_map.get(ch, 0) + 1
    
    unique_count = sum(1 for count in frequency_map.values() if count == 1)
    return unique_count


def main():
    s = "hello"
    print(solution(s))
    print(solution2(s))
    print(count_unique_characters(s))


if __name__ == "__main__":
    main()
