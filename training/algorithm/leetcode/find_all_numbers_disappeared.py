from typing import List


def find_all_numbers_disappeared(nums: List[int]) -> List[int]:
    """Find all numbers disappeared from array"""
    nums_set = set(nums)
    all_nums = set(range(1, len(nums) + 1))
    all_nums.difference_update(nums_set)
    return list(all_nums)


def main():
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    result = find_all_numbers_disappeared(nums)
    print(result)


if __name__ == "__main__":
    main()
