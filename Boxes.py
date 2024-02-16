import math


# Pre-processing to calculate values of memo[][]
def dfs(u, p, memo, lev, log, g):
    # Using recursion formula to calculate
    # the values of memo[][]
    memo[u][0] = p
    for i in range(1, log + 1):
        memo[u][i] = memo[memo[u][i - 1]][i - 1]

    for v in g[u]:
        if v != p:
            lev[v] = lev[u] + 1
            dfs(v, u, memo, lev, log, g)


# Function to return the LCA of nodes u and v
def lca(u, v, log, lev, memo):
    # The node which is present farthest
    # from the root node is taken as u
    # If v is farther from root node
    # then swap the two
    if lev[u] < lev[v]:
        temp = v
        v = u
        u = temp

    # Finding the ancestor of u
    # which is at same level as v
    for i in range(log, -1, -1):
        if (lev[u] - pow(2, i)) >= lev[v]:
            u = memo[u][i]

    # If v is the ancestor of u
    # then v is the LCA of u and v
    if u == v:
        return v

    # Finding the node closest to the
    # root which is not the common ancestor
    # of u and v i.e. a node x such that x
    # is not the common ancestor of u
    # and v but memo[x][0] is
    for i in range(log, -1, -1):
        if memo[u][i] != memo[v][i]:
            u = memo[u][i]
            v = memo[v][i]

    # Returning the first ancestor
    # of above found node
    return memo[u][0]


def main():
    n = int(input()) + 1
    log = math.ceil(math.log(n, 2))
    g = [[] for i in range(n + 1)]

    memo = [[-1 for i in range(log + 1)] for j in range(n + 1)]
    lev = [0 for i in range(n + 1)]

    things = list(map(int, input().split()))
    for i, thing in enumerate(things):
        i += 1
        g[i].append(thing)
        g[thing].append(i)
    dfs(1, 1, memo, lev, log, g)
        # for


if __name__ == "__main__":
    main()
