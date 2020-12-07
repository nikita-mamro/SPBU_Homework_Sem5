def count_rectangles(n):
    return int((n * (n + 1) / 2) ** 2)


def main():
    print(count_rectangles(5))


if __name__ == '__main__':
    main()
