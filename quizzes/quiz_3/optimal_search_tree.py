# This code might be buggy.

def optimal_search_tree_weight(a):
    a.sort()

    n = len(a)
    A = [[0] * n for i in range(n)] # Avoids pointer-related issues.

    for s in range(n):
        for i in range(n - s):
            current_min = float('inf')

            for r in range(i, i + s + 1):
                new_min = sum(a[i:i + s + 1])

                if r - 1 >= 0:
                    new_min += A[i][r - 1]

                try:
                    new_min += A[r + 1][i + s]
                except(IndexError):
                    pass
                finally:
                    if new_min < current_min:
                        current_min = new_min

            A[i][i + s] = round(current_min, 2)

    for row in A:
        print row

    return A[0][n - 1]

def main():
    a = [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]
    # print optimal_search_tree_weight(a)
    print optimal_search_tree_weight(a)

if __name__ == '__main__':
    main()