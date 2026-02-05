from typing import List, Optional


def product_except_self(nums: List[int]) -> Optional[List[int]]:
    """Calculate product of array except self (optimized)"""
    if not nums:
        return None
    
    answer = [0] * len(nums)
    tmp = 1
    
    # Calculate left products
    for i in range(len(nums)):
        answer[i] = tmp
        tmp *= nums[i]
    
    tmp = 1
    
    # Calculate right products and multiply with left
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= tmp
        tmp *= nums[i]
    
    return answer


def product_except_self1(nums: List[int]) -> Optional[List[int]]:
    """Calculate product of array except self (with separate left/right arrays)"""
    if not nums:
        return None
    
    left = [0] * len(nums)
    tmp = 1
    
    for i in range(len(nums)):
        left[i] = tmp
        tmp *= nums[i]
    
    tmp = 1
    right = [0] * len(nums)
    
    for i in range(len(nums) - 1, -1, -1):
        right[i] = tmp
        tmp *= nums[i]
    
    answer = [left[i] * right[i] for i in range(len(nums))]
    return answer


def main():
    nums = [1, 2, 3, 4]
    result = product_except_self1(nums)
    for val in result:
        print(val, end="")
    print()


if __name__ == "__main__":
    main()
