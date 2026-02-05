from typing import List


def sort_colors(nums: List[int]):
    """Sort colors (0, 1, 2) in-place"""
    p0 = 0
    curr = 0
    p2 = len(nums) - 1
    
    while curr <= p2:
        if nums[curr] == 0:
            nums[p0], nums[curr] = nums[curr], nums[p0]
            curr += 1
            p0 += 1
        elif nums[curr] == 2:
            nums[p2], nums[curr] = nums[curr], nums[p2]
            p2 -= 1
        else:
            curr += 1


def main():
    nums = [2, 0, 0, 1, 1, 2]
    sort_colors(nums)
    for val in nums:
        print(val, end="")
    print()


if __name__ == "__main__":
    main()
