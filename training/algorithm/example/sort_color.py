from typing import List


def sort_colors(colors: List[int]):
    """
    Sort an array containing 0s, 1s, and 2s in-place so that all 0s come first,
    followed by all 1s, and then all 2s
    Input: [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    """
    low = 0
    mid = 0
    high = len(colors) - 1
    
    while mid <= high:
        if colors[mid] == 0:
            colors[low], colors[mid] = colors[mid], colors[low]
            low += 1
            mid += 1
        elif colors[mid] == 1:
            mid += 1
        else:  # colors[mid] == 2
            colors[mid], colors[high] = colors[high], colors[mid]
            high -= 1


def sort_k_colors(colors: List[int], k: int):
    """Sort an array containing k different colors (0 to k-1)"""
    count = [0] * k
    
    for color in colors:
        count[color] += 1
    
    index = 0
    for i in range(k):
        for j in range(count[i]):
            colors[index] = i
            index += 1


def main():
    colors = [2, 0, 2, 1, 1, 0]
    sort_colors(colors)
    for color in colors:
        print(color, end=" ")
    print()
    
    colors_k = [3, 2, 1, 0, 4, 3, 2, 1, 0]
    k = 5
    sort_k_colors(colors_k, k)
    for color in colors_k:
        print(color, end=" ")
    print()


if __name__ == "__main__":
    main()
