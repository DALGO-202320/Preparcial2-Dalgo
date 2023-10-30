# Time Complexity - O(V + E)
# Good for finding the shortest path on unweighted graphs.

def bfs(V: int, E: int, graph: dict, start: int) -> None:
    queue = [start]
    visited = [False] * V
    while queue:
        current = queue.pop(0)
        visited[current] = True
        for edge in graph[current]:
            if not visited[edge[0]]:
                queue.append(edge[0])
    
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

print(bfs(V, E, adj_list, start))