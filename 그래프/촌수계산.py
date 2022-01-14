# https://www.acmicpc.net/problem/2644
import sys
from collections import deque
si = sys.stdin.readline

def main():
    n = int(si())
    s1, s2 = map(int, si().split())
    m = int(si())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, si().split())
        graph[x].append(y)
        graph[y].append(x)
    
    visited = [-1] * (n + 1)
    q = deque()
    q.append(s1)
    visited[s1] = 0
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if visited[nxt] != -1: continue
            visited[nxt] = visited[cur] + 1
            q.append(nxt)
    
    print(visited[s2])

if __name__ == "__main__":
    main()