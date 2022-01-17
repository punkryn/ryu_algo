# https://www.acmicpc.net/problem/11725
import sys
from collections import deque
si = sys.stdin.readline

def main():
    n = int(si())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, si().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (n + 1)
    q = deque()
    q.append(1)
    visited[1] = 1
    while q:
        cur = q.popleft()
        
        for nxt in graph[cur]:
            if visited[nxt] != 0: continue
            visited[nxt] = cur
            q.append(nxt)
    
    for ans in visited[2:]:
        print(ans)

if __name__ == '__main__':
    main()