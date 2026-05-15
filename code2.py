# Dijkstra Algorithm in Python

def dijkstra(graph, source):
    n = len(graph)
    distance = [float('inf')] * n
    visited = [False] * n

    distance[source] = 0

    for _ in range(n):
        # Find minimum distance vertex
        min_distance = float('inf')
        u = -1

        for i in range(n):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                u = i

        visited[u] = True

        # Update distances
        for v in range(n):
            if graph[u][v] > 0 and not visited[v]:
                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]

    # Print result
    print("Vertex \t Distance from Source")
    for i in range(n):
        print(i, "\t", distance[i])


# Graph represented as adjacency matrix
graph = [
    [0, 10, 0, 5, 0],
    [0, 0, 1, 2, 0],
    [0, 0, 0, 0, 4],
    [0, 3, 9, 0, 2],
    [7, 0, 6, 0, 0]
]

source = 0
dijkstra(graph, source)
