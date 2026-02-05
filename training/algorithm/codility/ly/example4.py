from typing import List


def solution(numbers: List[int], target: int) -> List[int]:
    """Two sum - find two numbers that add up to target"""
    numbers.sort()
    
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [numbers[left], numbers[right]]
        elif total < target:
            left += 1
        else:
            right -= 1
    
    return []


def main():
    numbers = [2, 7, 11, 15]
    target = 9
    print(solution(numbers, target))


if __name__ == "__main__":
    main()
