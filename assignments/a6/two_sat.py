from sys import path
from sets import Set

path.append('../utils')

from graph_utils import format_adjacency_list, add_unit_directed, add_unit_directed_reverse, dfs

# Special unit graph constructor for the 2-SAT problem.
def construct_unit_graph_two_sat(clauses, add_to_graph = add_unit_directed):
    g = {}

    for clause in clauses:
        literal_a = clause[0]
        literal_b = clause[1]

        # The two equivalent implications; at least one of them must hold.
        add_to_graph(g, -literal_a, literal_b) # If not a, then b.
        add_to_graph(g, -literal_b, literal_a) # If not b, then a.

    return g

def check_satisfaction(literal, leader, leaders):
    # The literal and its negation both belong to the same SCC,
    # therefore 2-SAT not satisfiable.
    if (-literal in leaders) and (leaders[-literal] == leader):
        return False

    leaders[literal] = leader

    return True

def kosarajus_two_sat(clauses, n):
    # First pass.
    g_rvs = construct_unit_graph_two_sat(clauses, add_unit_directed_reverse)
    explored = Set()
    finishing_order = []

    for i in range(-n, n + 1): # Yes this includes 0 but it won't matter.
        dfs(g_rvs, i, explored, lambda u: finishing_order.append(u))

    # Second pass.
    g = construct_unit_graph_two_sat(clauses)
    explored = Set()
    leaders = {} # NOTE: different structure from that of algorithms_i.

    for i in reversed(finishing_order):
        ans = dfs(g, i, explored, lambda u: check_satisfaction(u, i, leaders))

        # Halt early.
        if not ans:
            break

    return ans

def brute_force_verify(clauses, n):
    for candidate in range(1 << n):
        candidate_valid = True

        for clause in clauses:
            clause_satisfied = False

            for literal in clause:
                if not clause_satisfied: # Don't break satisfied clause.
                    if literal > 0:
                        clause_satisfied = candidate | (1 << (literal - 1)) == candidate
                    else:
                        clause_satisfied = candidate ^ (1 << (-literal - 1)) > candidate

            if not clause_satisfied:
                candidate_valid = False
                break

        if candidate_valid:
            return True

    return False

# Kind of pointless but "wrap-aliasing" for clarity.
def two_sat(clauses, n):
    return kosarajus_two_sat(clauses, n)

def main():
    c = None # Clauses.
    ans_arr = []

    for i in range(1, 7):
        # The custom output should be 101011.
        f = open('data/2sat%s.txt' % i)
        c = f.readlines()
        f.close()

        n = int(c[0])
        c = format_adjacency_list(c[1:])
        ans = two_sat(c, n)

        print ans

        # Convert boolean to integer,
        # then to string for concatenation.
        ans_arr.append(str(int(ans)))

    print '\n%s' % ''.join(ans_arr)

if __name__ == '__main__':
    main()