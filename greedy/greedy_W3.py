def construc(edges, total_nodes):
    adj = [[] for _ in range(total_nodes)]
    for u, v, wt in edges:
        adj[u].append((v, wt))
        adj[v].append((u, wt))  # สำหรับกราฟสองทาง
    return adj

def min_distance(dist, visited):
    min_val = float('inf')
    min_index = -1
    for i in range(len(dist)):
        if not visited[i] and dist[i] < min_val:
            min_val = dist[i]
            min_index = i
    return min_index

def dijkstra(total_nodes, edges, start, goal):
    adj = construc(edges, total_nodes)
    dist = [float('inf')] * total_nodes
    visited = [False] * total_nodes
    parent = [-1] * total_nodes

    dist[start] = 0

    for _ in range(total_nodes):
        u = min_distance(dist, visited)
        if u == -1:
            break
        visited[u] = True
        for v, weight in adj[u]:
            if not visited[v] and dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                parent[v] = u

    # Reconstruct path
    path = []
    cur = goal
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return dist[goal], path

# ทดสอบ
if __name__ == "__main__":
    start = 0
    goal = 6
    total_nodes = 9  # เพราะมี node ถึง 8
    edges = [
        [0, 1, 4],
        [0, 7, 8],
        [1, 7, 11],
        [1, 2, 8],
        [7, 8, 7],
        [7, 6, 1],
        [6, 8, 6],
        [8, 2, 2],
        [2, 5, 4],
        [2, 3, 7],
        [6, 5, 2],
        [3, 5, 14],
        [3, 4, 9],
        [5, 4, 10]
    ]

    cost, path = dijkstra(total_nodes, edges, start, goal)
    print("ระยะทางรวมสั้นที่สุด:", cost)
    print("เส้นทางที่ใช้:", " → ".join(map(str, path)))
