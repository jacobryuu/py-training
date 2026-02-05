from typing import List


def solution(A: List[str]) -> List[int]:
    """Cache operations simulator"""
    EVICT = "evict"
    ADD = "add"
    GET = "get"
    REMOVE = "remove"
    EXIT = "exit"
    
    max_key = 0
    result_list = []
    operate_map = {}
    
    for op in A:
        operate_arrays = op.split(" ")
        command = operate_arrays[0]
        
        if command == ADD:
            key = int(operate_arrays[1])
            value = int(operate_arrays[2])
            operate_map[key] = value
            max_key = key
        elif command == GET:
            key = int(operate_arrays[1])
            result_list.append(operate_map.get(key, -1))
        elif command == REMOVE:
            key = int(operate_arrays[1])
            if key in operate_map:
                result_list.append(operate_map.pop(key))
            else:
                result_list.append(-1)
        elif command == EXIT:
            break
        elif command == EVICT:
            if max_key in operate_map:
                del operate_map[max_key]
    
    return result_list


def main():
    operations = ["add 1 10", "add 2 20", "get 1", "get 3", "remove 2"]
    print(solution(operations))


if __name__ == "__main__":
    main()
