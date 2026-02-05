from typing import List


def solution(X: int, A: List[int]) -> int:
    """Find earliest time when frog can cross"""
    array_list = []
    total = 0
    
    for i in range(len(A)):
        if A[i] <= X and A[i] not in array_list:
            total += A[i]
            array_list.append(A[i])
        
        if A[i] == X:
            if total == X * (X + 1) // 2:
                return i
    
    return -1


def frog(X: int, A: List[int]) -> int:
    """Optimized version using bitmap"""
    steps = X
    bitmap = [False] * (steps + 1)
    
    for i in range(len(A)):
        if not bitmap[A[i]]:
            bitmap[A[i]] = True
            steps -= 1
            if steps == 0:
                return i
    
    return -1


def main():
    X = 5
    A = [1, 3, 1, 4, 2, 3, 5, 4]
    print(solution(X, A))  # 6
    print(frog(X, A))  # 6


if __name__ == "__main__":
    main()
