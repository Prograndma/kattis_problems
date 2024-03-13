def dfs(edges, node, visited):
    visited[node] = True
    for edge in edges:
        if node in edge:
            neighbor = edge[0] if edge[1] == node else edge[1]
            if not visited[neighbor]:
                dfs(edges, neighbor, visited)


def is_connected(edges, num_nodes):
    visited = [False] * num_nodes
    start_node = 0
    dfs(edges, start_node, visited)
    return all(visited)


def analyze_graph(num_nodes, num_edges):
    graph = [0 for _ in range(num_nodes)]
    connections = []
    for _ in range(0, num_edges):
        things = list(map(int, input().split()))
        edge1 = things[0]
        edge2 = things[1]
        graph[edge1] += 1
        graph[edge2] += 1
        connections.append([edge1, edge2])

    if any(num < 2 for num in graph):
        return "yes"
    if not is_connected(connections, num_nodes):
        return "yes"
    return "no"


def main():
    while True:
        things = list(map(int, input().split()))
        one = things[0]
        two = things[1]
        if one == 0 and two == 0:
            break
        print(analyze_graph(one, two))


if __name__ == "__main__":
    main()
