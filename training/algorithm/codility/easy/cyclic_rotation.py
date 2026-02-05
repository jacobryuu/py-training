from typing import List


def solution1(A: List[int], K: int) -> List[int]:
    """Rotate array using index calculation"""
    a_length = len(A)
    B = [0] * a_length
    
    for i in range(a_length):
        x = K + i
        if x >= a_length:
            x -= (round(x / a_length) * a_length)
        B[x] = A[i]
    
    return B


def solution(arrays: List[int], k: int) -> List[int]:
    """Rotate array by moving elements"""
    if len(arrays) <= 1:
        return arrays
    
    list_int = arrays[:]
    
    for _ in range(k):
        list_rotation = [list_int[-1]] + list_int[:-1]
        list_int = list_rotation
    
    return list_int


def main():
    A = [3, 8, 9, 7, 6]
    K = 3
    print(solution(A, K))  # [9, 7, 6, 3, 8]


if __name__ == "__main__":
    main()
