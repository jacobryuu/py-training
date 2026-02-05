from typing import List


def find_duplicate(nums: List[int]) -> int:
    """Find duplicate using HashMap"""
    seen = {}
    for num in nums:
        if num in seen:
            return num
        else:
            seen[num] = 1
    return -1


def find_duplicate2(nums: List[int]) -> int:
    """Find duplicate using Floyd's cycle detection"""
    slow = nums[0]
    fast = nums[0]
    
    # Find intersection point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Find entrance to cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow


def find_duplicate3(nums: List[int]) -> int:
    """Find duplicate by marking visited indices"""
    for i in range(len(nums)):
        index = abs(nums[i])
        if nums[index] < 0:
            return index
        nums[index] = -nums[index]
    return -1


def find_duplicate4(nums: List[int]) -> int:
    """Find duplicate using binary search"""
    left = 1
    right = len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        count = sum(1 for num in nums if num <= mid)
        
        if count > mid:
            right = mid
        else:
            left = mid + 1
    
    return left


def main():
    nums = [1, 3, 4, 2, 2]
    print(find_duplicate(nums))


if __name__ == "__main__":
    main()
