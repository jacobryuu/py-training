def century_from_year(year: int) -> int:
    return (year - 1) // 100 + 1


def main():
    year = 1000
    print(f"{century_from_year(year)}")


if __name__ == "__main__":
    main()
