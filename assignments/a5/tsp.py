from math import sqrt, floor
from sys import path

path.append('../utils')

from graph_utils import construct_graph

inf = float('inf')

# Expects tuple inputs.
def euclidian(a, b):
    delta_x = a[0] - b[0]
    delta_y = a[1] - b[1]

    return sqrt(pow(delta_x, 2) + pow(delta_y, 2))

def get_powers_of_2(n):
    return [1 << i for i in range(n)]

def tsp(g, n):
    global inf

    range_n = range(n)
    range_n_1 = range_n[1:] # Exclude starting point.
    powers_of_2 = get_powers_of_2(n)

    S = 3
    V = 1 << n

    # Compacted answer array (since we only care about odd S values).
    A = [[inf for i in range_n] for j in range(V >> 1)]

    V -= 1 # Now we convert it to a complete vertex set.
    A[0][0] = 0

    while S <= V:
        for j in range_n_1:
            candidates = [inf]
            powers_of_2_j = powers_of_2[j]

            if powers_of_2_j & S: # j in S.
                for k in range_n:
                    if (powers_of_2[k] & S) and k != j:
                        candidates.append(A[(S ^ powers_of_2_j) >> 1][k] + g[k][j])

                A[S >> 1][j] = min(candidates)

        S += 2 # Hit all the odd numbers.

    final_candidates = []
    V >>= 1 # Finally, we're going to use V as the last index of A.

    for j in range_n_1:
        final_candidates.append(A[V][j] + g[j][0]) # Homecoming.

    return min(final_candidates)

def main():
    f = open('data/tsp.txt')
    a = []

    for line in f:
        line = line.rstrip()
        if line:
            a.append(line)

    f.close()

    n = int(a[0])
    a = map(lambda x: tuple(map(float, x.split(' '))), a[1:])
    al = []

    for i in range(n):
        for j in range(i + 1, n):
            al.append((i, j, euclidian(a[i], a[j])))

    g = construct_graph(al, formatted = True)

    print tsp(g, n)

if __name__ == '__main__':
    main()