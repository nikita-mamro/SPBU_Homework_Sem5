def K(i, j):
    return (i + j - 1) * (i + j - 2) / 2 + j


def N(n):
    return n * (n + 1) / 2


def IJ(k):
    (i, j) = (1, 1)
    K = 1

    while (K != k):
        while (j <= i):
            k += 1
            j += 1
        i += 1
        j = 1

    return (i, j)


def main():
    for k in range(1, 16):
        (i, j) = IJ(k)
        print("I(", k, ") = ", i)
        print("J(", k, ") = ", j)


if __name__ == '__main__':
    main()
