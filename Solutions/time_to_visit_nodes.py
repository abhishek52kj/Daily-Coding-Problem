import heapq

def min_time_to_receive_message(N, edges):
    graph = {i: [] for i in range(N)}
    for a, b, t in edges:
        graph[a].append((b, t))
        graph[b].append((a, t))  # Adding edges for both directions

    # Dijkstra's algorithm
    min_time = [float('inf')] * N
    min_time[0] = 0
    pq = [(0, 0)]  # (time, node)

    while pq:
        time, node = heapq.heappop(pq)
        if time > min_time[node]:
            continue
        for neighbor, t in graph[node]:
            if time + t < min_time[neighbor]:
                min_time[neighbor] = time + t
                heapq.heappush(pq, (time + t, neighbor))

    return max(min_time)

# Example usage:
N = 6
edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
print(min_time_to_receive_message(N, edges))  # Output: 9
