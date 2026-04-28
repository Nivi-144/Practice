def prims(graph):
    n = len(graph)
    selected = [False] 
    edges = 0
    selected[0] = True
    print("Edge : Weight")
    while edges < n - 1:
        minimum = float('inf')
        x = 0
        y = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if (not selected[j]) and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j
        
        print(f"{x} - {y} : {graph[x][y]}")
        selected[y] = True
        edges += 1
