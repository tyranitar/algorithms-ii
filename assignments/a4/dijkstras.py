from heapq import heappush, heappop

inf = float('inf')

def absorb_vertex(g, u, h, A):
    global inf

    if u in g:
        g_u = g[u]

        for v in g_u:
            if A[v] == inf: # v yet to be explored.
                heappush(h, (A[u] + g_u[v], v))

# WARNING: assumes nodes are labelled in sequential order.
def dijkstras(g, s, n):
    global inf

    n_1 = n + 1
    A = [inf] * n_1 # Include 0th index for kicks.
    A[s] = 0
    h = [] # Heap.

    absorb_vertex(g, s, h, A)

    try:
        for i in range(n - 1): # Going to run exactly n - 1 times since we already have s.
            gs = None # Dijkstra's greedy score.
            v = None

            while True: # Not sure if loop needed.
                min_edge = heappop(h) # Will throw IndexError if further exploration is impossible.
                v = min_edge[1]

                if A[v] == inf: # v yet to be explored.
                    gs = min_edge[0]
                    break

            # Absorbing one new vertext per iteration.
            A[v] = gs
            absorb_vertex(g, v, h, A)
    except IndexError:
        pass

    return A