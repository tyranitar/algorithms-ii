import sys
sys.path.insert(0, '../utils')

from graph_utils import add_directed, add_directed_reverse, construct_graph
from bellman_ford import bellman_ford
from dijkstras import dijkstras

# WARNING: assumes that graphs are labelled in sequential order,
# and that the 0 label does not yet exist.
def add_dummy(g, n):
    g[0] = {}
    g_0 = g[0]

    for i in range(1, n + 1):
        g_0[i] = 0

# WARNING: assumes the same as above.
def add_dummy_reverse(g, n):
    for i in range(1, n + 1):
        if i not in g:
            g[i] = {}

        g[i][0] = 0

def reweight_edges(g, weights):
    for u in g:
        g_u = g[u]

        for v in g_u:
            g_u[v] += weights[u] - weights[v]

def johnsons(al, n):
    A = []
    g = construct_graph(al, add_directed)
    g_rvs = construct_graph(al, add_directed_reverse)
    add_dummy_reverse(g_rvs, n)
    weights = bellman_ford(g_rvs, 0, n)

    if weights:
        reweight_edges(g, weights)
    else:
        return weights

    labels = range(n + 1)

    for s in range(1, n + 1):
        dijkstras_result = dijkstras(g, s, n)

        # Weights will all be non-negative real numbers, which is why the lambda operation is safe.
        A.append(min(map(lambda x, i: x + weights[i] - weights[s], dijkstras_result, labels)))

    return min(A)

def main():
    file_name = None

    try:
        file_name = sys.argv[1]
    except IndexError:
        print "defaulting to g1"
        file_name = 'g1'

    f = open('data/%s.txt' % file_name)
    al = f.readlines()
    f.close()

    n_m = map(int, al[0].split(' '))
    n = n_m[0]
    m = n_m[1]
    al = al[1:]

    print johnsons(al, n)

if __name__ == '__main__':
    main()