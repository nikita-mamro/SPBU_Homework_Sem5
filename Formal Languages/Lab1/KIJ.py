def K(i, j):
    return (i + j - 1) * (i + j - 2) / 2 + j


def N(n):
    return n * (n + 1) / 2


def IJ(k):
    K = 0
    N = 1
    while (K != k):
        for j in range(1, N + 1):
            K += 1
            i = N + 1 - j
            if K == k:
                return (i, j)

        N += 1

    return (i, j)


def main():
    (i, j) = IJ(1000)
    print("(I, J) = ", (i, j))
    print("K = ", K(i, j))


if __name__ == '__main__':
    main()
