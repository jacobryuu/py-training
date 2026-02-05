from typing import List


def print_even():
    """Print even-indexed elements from comma-separated string"""
    s = "1,2,3,4,4,6,7"
    arr = s.split(",")
    
    result: List[str] = []
    
    if len(arr) == 0:
        pass
    elif len(arr) <= 2:
        result.append(arr[1])
    else:
        length = len(arr)
        
        i = 1
        while i < length:
            result.append(arr[i])
            if i + 1 < length and arr[i] == arr[i + 1]:
                result.append(arr[i + 1])
            i += 2
    
    for item in result:
        print(item, end="")


def main():
    print_even()


if __name__ == "__main__":
    main()
