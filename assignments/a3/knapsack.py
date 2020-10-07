def knapsack(W, n, a):
    a = [(0, 0)] + a
    A = [[0] * (W + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        v = a[i][0]
        w = a[i][1]

        for x in range(1, W + 1):
            added = 0
            x_w = x - w

            prev = A[i - 1][x]

            if x_w >= 0:
                added = A[i - 1][x_w] + v

            A[i][x] = max(prev, added)

    return A[n][W]

def main():
    f = open('data/_6dfda29c18c77fd14511ba8964c2e265_knapsack1.txt')
    a = f.readlines()
    f.close()

    a = map(lambda x: map(int, x.split(' ')), a)
    W = a[0][0]
    n = a[0][1]
    a = a[1:]

    print knapsack(W, n, a)

if __name__ == '__main__':
    main()