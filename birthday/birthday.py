class ThereIsABridge(Exception):
    pass


class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.nodes = [ [] for _ in range(self.num_nodes)]
        self.time = 0

    def add_connection(self, start, end):
        self.nodes[start].append(end)
        self.nodes[end].append(start)

    def get_connections(self, node, parent=None):
        if parent is not None:
            return self.nodes[:].remove(parent)     # a quick way to copy the list, and remove the parent.
        return self.nodes[node]

    def has_a_bridge(self):
        self.time = 0
        parent = [-1] * self.num_nodes
        visited = [False] * self.num_nodes
        disc = [self.num_nodes + 1] * self.num_nodes
        disc[0] = 0

        low = [self.num_nodes + 1] * self.num_nodes
        low[0] = 0
        try:
            for i in range(self.num_nodes):
                if not visited[i]:
                    self._bridge_helper(i, visited, parent, low, disc)
        except ThereIsABridge:
            return True
        return False

    def _bridge_helper(self, node, visited, parent, low, disc):
        visited[node] = True
        disc[node] = self.time
        low[node] = self.time
        self.time += 1

        for connected_node in self.nodes[node]:
            if not visited[connected_node]:
                parent[connected_node] = node
                self._bridge_helper(connected_node, visited, parent, low, disc)
                low[node] = min(low[node], low[connected_node])

                if low[connected_node] > disc[node]:
                    raise ThereIsABridge()
            elif connected_node != parent[node]:
                low[node] = min(low[node], disc[connected_node])


def analyze_graph(num_nodes, num_edges):
    my_graph = Graph(num_nodes)
    graph = [0 for _ in range(num_nodes)]
    for _ in range(0, num_edges):
        things = list(map(int, input().split()))
        edge1 = things[0]
        edge2 = things[1]
        graph[edge1] += 1
        graph[edge2] += 1
        my_graph.add_connection(edge1, edge2)

    if any(num < 2 for num in graph):       # quick first pass
        return "yes"
    if my_graph.has_a_bridge():
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
