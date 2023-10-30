# Time Complexity - O(VE)
# When Dijkstra fail. For example when negative edges.

def bellman_ford(V: int, E: int, graph: dict, start: int):
    distances = [float("inf")] * V
    distances[start] = 0
    predecessors = [-1] * V

    for _ in range(V - 1):
        for parent_node in graph:
            for next_node, weight in graph[parent_node]:
                if distances[parent_node] != float("inf") and distances[parent_node] + weight < distances[next_node]:
                    distances[next_node] = distances[parent_node] + weight
                    predecessors[next_node] = parent_node

    for parent_node in graph:
        for next_node, weight in graph[parent_node]:
            if distances[parent_node] != float("inf") and distances[parent_node] + weight < distances[next_node]:
                raise ValueError("Graph contains a negative weight cycle")
    
    return distances, predecessors
        
V = 6
E = 6
start = 0
adj_list = {
    0: [(2, 3), (4, 1), (3, 2)],
    1: [],
    2: [(4, 5)],
    3: [(4, 3)],
    4: [(5, 2)],
    5: [] 
}

print(bellman_ford(V, E, adj_list, start))