def find(parent,x: int) -> int:

    return # encuentra la "raíz" de un grupo al que pertenece el vértice x

def union(parent,rank,x: int,y: int) -> None:
    pass
    # une dos conjuntos. Cambia la "raíz" de un grupo para que ambos vértices tengan la misma "raíz", indicando que están en el mismo grupo.

def Kruskal(graph: list[list[int]], graph_nodes: int) -> int:
    total_cost = 0
    mst_value = 0
    graph.sort(key=lambda x:x[2]) 

    rank = [1] * graph_nodes
    parent = [i for i in range(graph_nodes)]

    for edge in graph:
        if find(parent, edge[0]) != find(parent, edge[1]):
            total_cost += edge[2]
            mst_value += edge[2]
            union(parent, rank, edge[0],edge[1])
        else:
            total_cost += edge[2]
    return total_cost-mst_value