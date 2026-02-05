from typing import List


def solution1(arrays: List[int]) -> int:
    """Calculate minimum difference (naive approach)"""
    if len(arrays) >= 100000 or len(arrays) == 0:
        return 0
    
    result = []
    for i in range(len(arrays) - 1):
        first = arrays[:i + 1]
        second = arrays[i + 1:]
        result.append(abs(sum(first) - sum(second)))
    
    return min(result)


def solution(arrays: List[int]) -> int:
    """Calculate minimum difference (optimized)"""
    right_sum = 0
    left_sum = 0
    
    left_sum = arrays[0]
    
    for i in range(1, len(arrays)):
        right_sum += arrays[i]
    
    mini = abs(right_sum - left_sum)
    
    for P in range(1, len(arrays)):
        if abs(right_sum - left_sum) < mini:
            mini = abs(right_sum - left_sum)
        left_sum += arrays[P]
        right_sum -= arrays[P]
    
    return mini


def main():
    A = [3, 1, 2, 4, 3]
    print(solution(A))  # 1


if __name__ == "__main__":
    main()
