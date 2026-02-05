from sortedcontainers import SortedDict
from bisect import bisect_left
from typing import List, Tuple


class ReserveManagement:
    def __init__(self):
        self.reservations = SortedDict()
        self.bookings: List[Tuple[int, int]] = []
    
    @staticmethod
    def reserve(reservations: SortedDict, start: int, end: int) -> bool:
        """線形探索で予約を管理"""
        if start >= end:
            return False
        
        # Find previous reservation
        idx = reservations.bisect_left(start)
        if idx > 0:
            prev_start = reservations.keys()[idx - 1]
            prev_end = reservations[prev_start]
            if start < prev_end:
                return False
        
        # Find next reservation
        if idx < len(reservations):
            next_start = reservations.keys()[idx]
            if end > next_start:
                return False
        
        reservations[start] = end
        return True
    
    @staticmethod
    def reserve_binary(bookings: List[Tuple[int, int]], start: int, end: int) -> bool:
        """二分探索で予約を管理"""
        if start >= end:
            return False
        
        # Binary search for insertion position
        left, right = 0, len(bookings)
        while left < right:
            mid = (left + right) // 2
            if bookings[mid][0] < start:
                left = mid + 1
            else:
                right = mid
        idx = left
        
        # Check previous reservation
        if idx > 0 and start < bookings[idx - 1][1]:
            return False
        
        # Check next reservation
        if idx < len(bookings) and end > bookings[idx][0]:
            return False
        
        bookings.insert(idx, (start, end))
        return True


def main():
    reservations = SortedDict()
    print(ReserveManagement.reserve(reservations, 10, 20))  # True
    print(ReserveManagement.reserve(reservations, 15, 25))  # False
    print(ReserveManagement.reserve(reservations, 20, 30))  # True
    
    bookings: List[Tuple[int, int]] = []
    print(ReserveManagement.reserve_binary(bookings, 10, 20))  # True
    print(ReserveManagement.reserve_binary(bookings, 15, 25))  # False
    print(ReserveManagement.reserve_binary(bookings, 20, 30))  # True


if __name__ == "__main__":
    main()
