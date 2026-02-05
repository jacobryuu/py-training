from typing import List


def solution(words: List[str]) -> str:
    """Interleave words by taking characters from each word vertically"""
    max_length = max(len(word) for word in words) if words else 0
    
    result = []
    
    for i in range(max_length):
        for word in words:
            if i < len(word):
                result.append(word[i])
    
    return ''.join(result)


def main():
    words = ["abc", "de", "fghi"]
    print(solution(words))


if __name__ == "__main__":
    main()
