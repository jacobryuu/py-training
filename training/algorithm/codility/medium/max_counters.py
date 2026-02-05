from typing import List


def solution1(N: int, A: List[int]) -> List[int]:
    """MaxCounters solution (naive approach)"""
    res = [0] * N
    max_value = 0
    
    for a in A:
        if a == N + 1:
            res = [max_value] * N
        else:
            res[a - 1] += 1
            max_value = max(max_value, res[a - 1])
    
    return res


def solution(N: int, A: List[int]) -> List[int]:
    """MaxCounters solution (optimized)"""
    res = [0] * N
    current_maximum_value = 0
    min_value = 0
    
    for i in range(len(A)):
        if A[i] == N + 1:
            if min_value < current_maximum_value:
                min_value = current_maximum_value
        else:
            if res[A[i] - 1] < min_value:
                res[A[i] - 1] = min_value
            res[A[i] - 1] += 1
            if res[A[i] - 1] > current_maximum_value:
                current_maximum_value = res[A[i] - 1]
    
    for j in range(len(res)):
        res[j] = min_value if res[j] < min_value else res[j]
    
    return res


def main():
    N = 5
    A = [3, 4, 4, 6, 1, 4, 4]
    print(solution(N, A))  # [3, 2, 2, 4, 2]


if __name__ == "__main__":
    main()
