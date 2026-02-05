def count_word():
    """Count words starting with uppercase letter or digit"""
    test_str = "Providing medical-related services through the use of the Internet since 2000."
    
    arr = test_str.split(" ")
    
    if len(arr) == 0:
        print(0)
    else:
        arr_distinct = list(set(arr))
        cnt = 0
        
        for word in arr_distinct:
            if word:
                target = word[0]
                if target.isupper() or target.isdigit():
                    cnt += 1
        print(cnt)


def main():
    count_word()


if __name__ == "__main__":
    main()
