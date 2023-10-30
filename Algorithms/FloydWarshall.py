# Time Complexity - O(n3)

def floyd_warshall(graph: list[list[int]]):
    graph_size = len(graph)
    for initial in range(graph_size) :
        for middle in range(graph_size) :
            for end in range(graph_size) :
                graph[initial][end] = min(graph[initial][end], graph[initial][middle] + graph[middle][end])
    return graph

def floyd_warshall(graph: list[list[int]]):
    graph_size = len(graph)
    for middle in range(graph_size):
        for initial in range(graph_size):
            for end in range(graph_size):
                graph[initial][end] = min(graph[initial][end], graph[initial][middle] + graph[middle][end])
    return graph

if __name__ == '__main__':
    inf = 2 ** 64
    # current_graph =[
    #     [0,1,inf,inf],
    #     [4,0,3,inf],
    #     [-1,inf,0,-2],
    #     [inf,2,2,0]
    # ]
    
    current_graph =[
        [0,10,inf,inf],
        [inf,0,20,inf],
        [inf,inf,0,30],
        [-60,inf,inf,inf]
    ]
    apsp = floyd_warshall(current_graph)
    print(apsp)
    for row in apsp:
        print(' '.join(map(str,row)))