from typing import List
from collections import deque


def solution(capacity: int, commands: List[str]) -> List[str]:
    """Queue operations simulator"""
    queue = deque()
    result = []
    
    for cmd in commands:
        parts = cmd.split(" ", 1)
        command = parts[0]
        
        if command == "OFFER":
            if len(parts) > 1 and len(queue) < capacity:
                queue.append(parts[1])
                result.append("true")
            else:
                result.append("false")
        elif command == "TAKE":
            if queue:
                result.append(queue.popleft())
            else:
                result.append("false")
        elif command == "SIZE":
            result.append(str(len(queue)))
        else:
            raise ValueError(f"Unknown command: {cmd}")
    
    return result


def main():
    commands = ["OFFER item1", "OFFER item2", "TAKE", "SIZE"]
    print(solution(2, commands))


if __name__ == "__main__":
    main()
