# Time Complexity - O(V + E)

def dfs(V: int, E: int, graph: dict, start: int) -> None:
    stack = [start]
    visited = [False] * V
    while stack:
        current = stack.pop(-1)
        visited[current] = True
        for edge in graph[start]:
            if not visited[edge[0]]:
                stack.append(edge[0])

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

print(dfs(V, E, adj_list, start))