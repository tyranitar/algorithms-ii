import sys

from knapsack import knapsack

def cantor_pair(a, b):
    # This will always be an integer anyways.
    return int((0.5) * (a + b) * (a + b + 1) + b)

def knapsack_big(i, x, a, d = {}):
    if i < 0 or x < 0:
        return 0

    cp = cantor_pair(i, x)

    if cp in d:
        return d[cp]

    v = a[i][0]
    w = a[i][1]
    x_w = x - w

    prev = knapsack_big(i - 1, x, a, d)
    added = 0

    if x_w >= 0:
        added = knapsack_big(i - 1, x_w, a, d) + v

    ans = max(prev, added)
    d[cp] = ans

    return ans

def main():
    f = open('data/_6dfda29c18c77fd14511ba8964c2e265_knapsack_big.txt')
    a = f.readlines()
    f.close()

    a = map(lambda x: map(int, x.split(' ')), a)
    W = a[0][0]
    n = a[0][1]
    a = a[1:]

    sys.setrecursionlimit(W)
    print knapsack_big(n - 1, W, a)

if __name__ == '__main__':
    main()