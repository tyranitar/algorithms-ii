# WARNING: takes graphs with edge directions reversed for convenience.
# Current implementation also assumes s = 0.
def bellman_ford(g, s, n):
    # Initialize; include 0th index for kicks.
    n_1 = n + 1
    V = range(n_1)

    prev = [float('inf')] * n_1
    cur = prev[:]

    cur[s] = 0 # Since prev and cur get swapped in the first iteration.
    ret = None

    # Main loop, from 0 to n (since we include invisible vertex 0).
    for i in V:
        # Swap prev and cur pointers.
        temp = prev
        prev = cur
        cur = temp

        changed = False

        for v in V:
            case_1 = prev[v]
            case_2 = float('inf')

            if v in g: # v has at least one inward arc.
                g_v = g[v]
                tails = g_v.keys()
                case_2 = min(map(lambda tail: prev[tail] + g_v[tail], tails)) # g_v[tail] is the edge length.

            cur[v] = min(case_1, case_2)

            if cur[v] != case_1 and not changed:
                changed = True

        if changed:
            if i == n: # Negative cycle.
                ret = False
        else: # Break out early.
            ret = cur
            break

    return ret