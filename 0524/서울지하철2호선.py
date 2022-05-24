# https://www.acmicpc.net/problem/16947
import sys
from collections import deque
si = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def DFS(x, start, cnt):
    global isCycle
    if x == start and cnt >= 2:
        isCycle = True
        return
    
    visited[x] = True
    for nxt in graph[x]:
        if not visited[nxt]:
            DFS(nxt, start, cnt + 1)
        else:
            if nxt == start and cnt >= 2:
                DFS(nxt, start, cnt)
        
        if isCycle: return

def BFS(x):
    q = deque()
    q.append(x)
    visited = [-1] * (n + 1)
    visited[x] = 0
    while q:
        cur = q.popleft()
        if cycle_station[cur]:
            return visited[cur]

        for nxt in graph[cur]:
            if visited[nxt] != -1: continue
            visited[nxt] = visited[cur] + 1
            q.append(nxt)
    return 0

if __name__ == '__main__':
    n = int(si())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n):
        x, y = map(int, si().split())
        graph[x].append(y)
        graph[y].append(x)
    
    cycle_station = [False] * (n + 1)
    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        isCycle = False
        DFS(i, i, 0)
        if isCycle:
            cycle_station[i] = True
    
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        if not cycle_station[i]:
            ans[i] = BFS(i)
    print(*ans[1:])