from sets import Set
from cluster import UnionFind

# bs = bitstring
# idx = index to xor
def xor_bit(bs, idx):
    xored = str(int(bs[idx]) ^ 1)
    return bs[:idx] + xored + bs[idx + 1:]

def cluster_big(nodes, sz, nb):
    ufs = map(UnionFind, nodes)
    nodes_hash = {}
    k = sz

    for uf in ufs:
        nodes_hash[uf.value] = uf # Bitstring points to UnionFind object.

    def try_union(uf, xored):
        if xored in nodes_hash:
            if (uf.union(nodes_hash[xored])):
                return 1
        return 0

    for uf in ufs:
        for i in range(nb):
            bs = uf.value
            single_xored = xor_bit(bs, i)
            k -= try_union(uf, single_xored)

            for j in range(i + 1, nb):
                double_xored = xor_bit(single_xored, j)
                k -= try_union(uf, double_xored)

    return k

def main():
    f = open('data/_fe8d0202cd20a808db6a4d5d06be62f4_clustering_big.txt')
    nodes = f.readlines()
    f.close()
    fl = map(int, nodes[0].split(' ')) # First line.
    sz = fl[0] # Size of problem.
    nb = fl[1] # Number of bits.
    nodes = map(lambda x: x.replace(' ', '').replace('\n', ''), nodes[1:])
    nodes_unique = list(Set(nodes))
    num_dupes = len(nodes) - len(nodes_unique)

    # Duplicates will always be connected to each other.
    # This is the true value of k.
    print cluster_big(nodes_unique, sz, nb) - num_dupes

if __name__ == '__main__':
    main()