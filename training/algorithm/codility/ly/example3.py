from typing import List
from collections import deque


def solution(window_size: int, numbers: List[int]) -> List[int]:
    """Sliding window maximum"""
    if not numbers or window_size <= 0:
        return []
    
    result = []
    dq = deque()
    
    for i in range(len(numbers)):
        # Remove elements outside window
        if dq and dq[0] < i - window_size + 1:
            dq.popleft()
        
        # Remove smaller elements from back
        while dq and numbers[dq[-1]] <= numbers[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add to result when window is full
        if i >= window_size - 1:
            result.append(numbers[dq[0]])
    
    return result


def main():
    numbers = [1, 3, -1, -3, 5, 3, 6, 7]
    window_size = 3
    print(solution(window_size, numbers))


if __name__ == "__main__":
    main()
