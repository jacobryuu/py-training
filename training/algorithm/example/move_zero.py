from typing import List


def move_zeroes_to_end(nums: List[int]):
    """
    Move all zeroes in the array to the end while maintaining the order of non-zero elements
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
    """
    not_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[not_zero_index], nums[i] = nums[i], nums[not_zero_index]
            not_zero_index += 1


def move_zeroes_to_end2(nums: List[int]):
    """Alternative implementation"""
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1


def remove_zeroes(nums: List[int]) -> List[int]:
    """
    Remove all zeroes from the array and return a new array with only non-zero elements
    """
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    return nums[:insert_pos]


def sub_array(nums: List[int], k: int) -> List[List[int]]:
    """Return all sub-arrays of size k from the given array"""
    result = []
    for i in range(len(nums) - k + 1):
        result.append(nums[i:i + k])
    return result


def move_zeroes_for_string(s: str) -> str:
    """Move all '0' characters to the end of the string"""
    result = []
    zero_count = 0
    for c in s:
        if c == '0':
            zero_count += 1
        else:
            result.append(c)
    result.extend(['0'] * zero_count)
    return ''.join(result)


def main(args=None):
    nums = [0, 1, 0, 3, 12]
    result = remove_zeroes(nums[:])
    for rst in result:
        print(rst, end=" ")
    print()
    
    nums2 = [0, 1, 0, 3, 12]
    result = sub_array(nums2, 2)
    print(f"result = {result}")
    
    s = "a0b0c0d"
    result_str = move_zeroes_for_string(s)
    print(f"resultStr = {result_str}")


if __name__ == "__main__":
    main()
