from typing import List


def solution(A: List[int]) -> int:
    """Find maximum product of three numbers"""
    if len(A) < 3:
        return -1
    
    A.sort()
    length = len(A)
    
    if A[length - 1] < 0:
        return A[length - 1] * A[length - 2] * A[length - 3]
    
    p1 = A[length - 1] * A[length - 2] * A[length - 3]
    p2 = A[length - 1] * A[0] * A[1]
    
    return max(p1, p2)


def main():
    A = [-10, -10, 1, 3, 2]
    print(solution(A))  # 300


if __name__ == "__main__":
    main()
