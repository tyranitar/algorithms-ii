import sys
sys.path.insert(0, '../assignment_1')

from prims import format_adjacency_list

class Group:
    def __init__(self, uf):
        self.ufs = [uf]
        self.size = 1

    def absorb(self, group):
        for uf in group.ufs:
            uf.group = self # Change leaders.

        self.ufs.extend(group.ufs) # Take all ufs.
        self.size += group.size # Update size.

class UnionFind:
    def __init__(self, val):
        self.value = val
        self.group = Group(self)

    # Union with another node
    def union(self, uf):
        group_a = self.group
        group_b = uf.group

        if group_a != group_b:
            if group_a.size >= group_b.size:
                group_a.absorb(group_b)
            else:
                group_b.absorb(group_a)
            return True # Successfully merged.
        else:
            return False # Merge did not happen.

    def find(self):
        return self.group

def reformat_adjacency_list(al):
    return map(lambda x: (x[2], x[0], x[1]), al)

def cluster(al, pa, sz, k):
    done_merging = False
    s = None

    for adjacency in al:
        uf_a = pa[adjacency[1]]
        uf_b = pa[adjacency[2]]

        if not done_merging:
            if uf_a.union(uf_b):
                sz -= 1 # Number of clusters decreases by 1 each time two groups are merged.

                if sz <= k:
                    done_merging = True
        else: # Keep iterating until first acyclic edge comes up.
            if uf_a.find() != uf_b.find():
                s = adjacency[0]
                break

    return s

def main():
    k = 4
    f = open('data/_fe8d0202cd20a808db6a4d5d06be62f4_clustering1.txt')
    al = f.readlines()
    f.close()
    sz = int(al[0]) # Size of problem.
    pa = map(lambda x: UnionFind(x), list(range(sz + 1))) # Pointer array.
    al = format_adjacency_list(al[1:])
    al = reformat_adjacency_list(al)
    al = sorted(al)

    print cluster(al, pa, sz, k)

if __name__ == '__main__':
    main()