def dfs(graph, node, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited = dfs(graph, neighbor, visited)
    return visited


def can_conquer(num_gym_leaders, rival_leader, alliances):
    graph = [[] for _ in range(num_gym_leaders + 1)]

    for alliance in alliances:
        leader1, leader2 = alliance
        graph[leader1].append(leader2)
        graph[leader2].append(leader1)

    visited = [False] * (num_gym_leaders + 1)
    dfs(graph, rival_leader, visited)

    has_changed = True
    while has_changed:
        if len(graph[rival_leader]) <= 1:
            return "YES"

        has_changed = False
        for i, connections in enumerate(graph):
            if len(connections) == 1:
                graph[connections[0]].remove(i)
                graph[i] = []
                has_changed = True

        visited = [False] * (num_gym_leaders + 1)
        for i, leader in enumerate(dfs(graph, rival_leader, visited)):
            if not leader:
                graph[leader] = []

    return "NO"


def main():
    n, rival, m = map(int, input().split())
    alliances = [tuple(map(int, input().split())) for _ in range(m)]

    result = can_conquer(n, rival, alliances)
    print(result)


if __name__ == "__main__":
    main()
