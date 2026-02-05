def solution(current: int, destination: int, distance: int) -> int:
    """Calculate minimum number of jumps for frog"""
    step = (destination - current) // distance
    return step if step * distance == (destination - current) else step + 1


def main():
    X = 10
    Y = 85
    D = 30
    print(solution(X, Y, D))  # 3


if __name__ == "__main__":
    main()
