from sets import Set

def add_to_graph(graph, node_a, node_b, edge_len):
    if node_a not in graph:
        graph[node_a] = {}

    if node_b not in graph:
        graph[node_b] = {}

    graph[node_a][node_b] = edge_len
    graph[node_b][node_a] = edge_len

def format_adjacency_list(adjacency_list):
    return map(lambda x: tuple(map(lambda y: int(y), x.split(' '))), adjacency_list)

def construct_graph(adjacency_list):
    graph = {}

    al_len = len(adjacency_list)

    for i in range(al_len):
        adjacency = adjacency_list[i]
        node_a = adjacency[0]
        node_b = adjacency[1]
        edge_len = adjacency[2]

        add_to_graph(graph, node_a, node_b, edge_len)

    return graph

def prims(graph):
    graph_keys = graph.keys()
    s = graph_keys[0] # Source node.
    X = Set([s])
    n = len(graph_keys) - 1 # Since we already added s.
    MST_len = 0

    while n > 0:
        min_edge_len = float('inf')
        min_edge_v = None

        for x in X:
            node = graph[x]

            for v in node.keys():
                if v in X:
                    del node[v] # Remove internal connection for faster computing.
                else: # In uncharted region.
                    edge_len = node[v]

                    if edge_len < min_edge_len:
                        min_edge_len = edge_len
                        min_edge_v = v

        X.add(min_edge_v) # Absorbtion.
        MST_len += min_edge_len

        n -= 1

    return MST_len

def main():
    f = open('data/_d4f3531eac1d289525141e95a2fea52f_edges.txt')
    al = f.readlines()
    f.close()
    al = format_adjacency_list(al[1:])
    graph = construct_graph(al)
    MST_len = prims(graph)

    print MST_len

if __name__ == '__main__':
    main()