n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
from collections import defaultdict
def validTree(n, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n
    def recur(node, parent, visited):
        visited[node] = True
        for child in adj[node]:
            if not visited[child]:
                if not recur(child, node, visited):
                    return False
            elif child != parent:
                return False
        return True
    return recur(0, -1, visited) and all(visited)
print(validTree(n, edges))