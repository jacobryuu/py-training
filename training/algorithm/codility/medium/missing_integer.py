from typing import List


def solution(nums: List[int]) -> int:
    """Find smallest positive integer not in array"""
    length = len(nums)
    visit = [False] * (length + 2)
    
    for num in nums:
        if 0 < num <= length:
            visit[num] = True
    
    for i in range(1, length + 2):
        if not visit[i]:
            return i
    
    return length + 1


def main():
    A = [1, 3, 6, 4, 1, 2]
    print(solution(A))  # 5


if __name__ == "__main__":
    main()
