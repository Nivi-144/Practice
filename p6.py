V = 
graph = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
]
path = [-1] * V
def isSafe(v, pos):
    if graph[path[pos-1]][v] == 0:
        return False
    if v in path:
        return False
    return True
def hamCycleUtil(pos):
    if pos == V:
        return graph[path[pos-1]][path[0]] == 1
    for v in range(1, V):
        if isSafe(v, pos):
            path[pos] = v
            if hamCycleUtil(pos+1):
                return True
            path[pos] = -1
    return False
def hamCycle():
    path[0] = 0
    if not hamCycleUtil(1):
        print("No Hamiltonian Cycle")
        return
    print("Hamiltonian Cycle:", path + [path[0]])
hamCycle()
