from typing import List


def solution(nums: List[int]) -> int:
    """Check if array is a permutation"""
    length = len(nums)
    visit = [False] * (length + 1)
    
    for num in nums:
        if 0 < num <= length:
            visit[num] = True
    
    for i in range(1, length + 1):
        if not visit[i]:
            return 0
    
    return 1


def main():
    A = [4, 1, 3, 2]
    print(solution(A))  # 1


if __name__ == "__main__":
    main()
