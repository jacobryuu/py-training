from typing import List
from collections import defaultdict


def can_form_pairs(shoes: List[List[int]]) -> bool:
    """Check if shoes can form pairs"""
    shoe_count = defaultdict(lambda: [0, 0])
    
    for shoe in shoes:
        shoe_type = shoe[0]  # 0: left, 1: right
        size = shoe[1]
        shoe_count[size][shoe_type] += 1
    
    for counts in shoe_count.values():
        if counts[0] != counts[1]:
            return False
    
    return True


def main():
    shoes1 = [[0, 21], [1, 23], [1, 21], [0, 23]]
    shoes2 = [[0, 21], [1, 23], [1, 21], [1, 23]]
    
    print(can_form_pairs(shoes1))  # True
    print(can_form_pairs(shoes2))  # False


if __name__ == "__main__":
    main()
