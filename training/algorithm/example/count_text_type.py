import re


def count_text_type(text: str) -> int:
    """
    Count words starting with uppercase letter or digit
    """
    count = 0
    split_str = re.split(r'\s+', text)
    
    for s in split_str:
        if s:
            first_char = s[0]
            if first_char.isupper() or first_char.isdigit():
                count += 1
    return count


def main():
    text = "Hello world 123 apple Banana. 4567 grape."
    result = count_text_type(text)
    print(f"Count of words starting with uppercase letter or digit:  {result}")


if __name__ == "__main__":
    main()
