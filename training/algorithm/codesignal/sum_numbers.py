#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solution(numbers: int) -> int:
    numbers = abs(numbers)
    result = 0
    while numbers > 0:
        result += numbers % 10
        numbers //= 10
    return result


def main() -> None:
    print(solution(1111111111111))

if __name__ == "__main__":
    main()
