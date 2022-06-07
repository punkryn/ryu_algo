# https://www.acmicpc.net/problem/1613
import sys
si = sys.stdin.readline

def dfs(x):
    if not edges[x]:
        for nxt in graph[x]:
            edges[x].add(nxt)
            edges[x] |= dfs(nxt)
    return edges[x]

if __name__ == '__main__':
    n, k = map(int, si().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        a, b = map(int, si().split())
        graph[a].append(b)
    
    edges = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        if not edges[i]:
            dfs(i)
    
    for _ in range(int(si())):
        a, b = map(int, si().split())
        if a in edges[b]:
            print(1)
        elif b in edges[a]:
            print(-1)
        else:
            print(0)

    # graph = [[0] * (n + 1) for _ in range(n + 1)]

    # for _ in range(k):
    #     a, b = map(int, si().split())
    #     graph[a][b] = -1
    #     graph[b][a] = 1
    
    # for k in range(1, n + 1):
    #     for i in range(1, n + 1):
    #         for j in range(1, n + 1):
    #             if graph[i][k] == 1 and graph[k][j] == 1:
    #                 graph[i][j] = 1
    #             elif graph[i][k] == -1 and graph[k][j] == -1:
    #                 graph[i][j] = -1
    
    # for _ in range(int(si())):
    #     a, b = map(int, si().split())
    #     print(graph[a][b])