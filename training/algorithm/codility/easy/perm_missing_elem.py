from typing import List


def solution(nums: List[int]) -> int:
    """Find missing element in permutation"""
    length = len(nums)
    visit = [False] * (length + 2)
    
    for num in nums:
        if 0 < num <= length + 1:
            visit[num] = True
    
    for i in range(1, length + 2):
        if not visit[i]:
            return i
    
    return length + 1


def main():
    A = [2, 3, 1, 5]
    print(solution(A))  # 4


if __name__ == "__main__":
    main()
