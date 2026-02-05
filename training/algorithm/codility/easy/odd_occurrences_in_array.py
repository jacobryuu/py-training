from typing import List


def solution(arrays: List[int]) -> int:
    """Find unpaired element using XOR"""
    result = 0
    for array in arrays:
        result = result ^ array
    return result


def main():
    A = [9, 3, 9, 3, 9, 7, 9]
    print(solution(A))  # 7


if __name__ == "__main__":
    main()
