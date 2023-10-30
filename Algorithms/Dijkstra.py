# Time Complexity - O(E * Log(V))

def dijkstra(V: int, E: int, graph: dict, start: int) -> None:
    distances = [float("inf")] * V
    distances[start] = 0
    pq = [(start, 0)]
    
    while pq:
        index, minValue = pq.pop(0)
        for neighbor, weight in graph[index]:
            newDist = distances[index] + weight
            if newDist < distances[neighbor]:
                distances[neighbor] = newDist
                pq.append((neighbor, newDist))
    return distances
        
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

print(dijkstra(V, E, adj_list, start))



# import heapq

# def make_graph():
#     # identical graph as the YouTube video: https://youtu.be/_lHSawdgXpI
#     # tuple = (cost, to_node)
#     return {1: [(1, 2), (1, 3)], 2: [(1, 1), (1, 3)], 3: [(1, 1), (1, 2)]}


# def dijkstraMaster(grafo, inicio):
#     #print(grafo)
#     distancias = {}
#     parent = {}

#     cola = [(0,inicio)]
#     for nodo in grafo:
#         if(nodo == inicio):
#             print(nodo)
#             distancias[nodo] = 0
#             parent[nodo] = 0
#         else:
#             distancias[nodo] = float('inf')
#             parent[nodo] = float('inf')

#     #1. Nodos adyacentes

#     while cola:
#         distancia, nodo = heapq.heappop(cola)
#         #print(nodo)
#         #minDist = (float('inf'), float('inf'))
#         for adyacente in grafo[nodo]:

#                 #print(adyacente)
#             #2. Costo de cada nodo adyacente, si la suma del costo actual mas el costo de ir es menor al costo registrado en la lista de distancias se cambia
#                 if distancias[nodo] + adyacente[0] < distancias[adyacente[1]]:
#                     distancias[adyacente[1]] = distancias[nodo] + adyacente[0]
#                     parent[adyacente[1]] = nodo
#                     heapq.heappush(cola, (distancias[adyacente[1]], adyacente[1]))

#         #visitados.append(nodo)

#         #print(distancias)
#         #print(visitados)



#     #print(distancias)
#     return parent



# def main():


#     grafo = make_graph()
#     start = 1

#     print(dijkstraMaster(grafo,start))

# main()