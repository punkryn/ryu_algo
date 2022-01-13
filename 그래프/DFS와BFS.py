# https://www.acmicpc.net/problem/1260

import sys
from collections import deque
si = sys.stdin.readline

def dfs(v, visited, graph):
    print(v, end=' ')
    for nxt in sorted(graph[v]):
        if visited[nxt] == 0:
            visited[nxt] = 1
            dfs(nxt, visited, graph)

def bfs(v, graph, n):
    visited = [0] * (n + 1)
    q = deque()
    q.append(v)
    while q:
        cur = q.popleft()
        if visited[cur] == 0:
            visited[cur] = 1
            print(cur, end=' ')
        else:
            continue
        
        for nxt in sorted(graph[cur]):
            if visited[nxt] == 0:
                q.append(nxt)

def main():
    n, m, v = map(int, si().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, si().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (n + 1)
    visited[v] = 1
    dfs(v, visited, graph)
    print()
    bfs(v, graph, n)

if __name__ == '__main__':
    main()