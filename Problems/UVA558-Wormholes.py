# https://vjudge.net/problem/UVA-558

import sys

def bellman_ford(graph: dict, start: int, num_vertices: int) -> bool:
    distances = [float("inf")] * num_vertices
    distances[start] = 0
    
    for _ in range(num_vertices - 1):
        for x in graph:
            for y, t in graph[x]:
                if distances[x] != float("inf") and distances[x] + t < distances[y]:
                    distances[y] = distances[x] + t
    
    for x in graph:
        for y, t in graph[x]:
            if distances[x] != float("inf") and distances[x] + t < distances[y]:
                return True  
    return False 

def main() -> None:
    c = int(sys.stdin.readline())
    for _ in range(c):
        n, m = map(int, sys.stdin.readline().split(" "))
        star_systems = {num: [] for num in range(n)}
        for wormhole in range(m):
            x, y, t = map(int, sys.stdin.readline().split())
            star_systems[x].append((y, t))
        res = bellman_ford(star_systems, 0, n)
        if res:
            print("possible")
        else:
            print("not possible")

if __name__ == "__main__":
    main()
