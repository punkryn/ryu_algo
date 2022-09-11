# https://www.acmicpc.net/problem/2660
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())
    edges = [[] for _ in range(n + 1)]
    while True:
        x, y = mis()
        if x == -1 and y == -1:
            break
        
        edges[x].append(y)
        edges[y].append(x)
    
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        q = deque([i])
        visited = [-1] * (n + 1)
        visited[i] = 0
        
        score = 0
        while q:
            x = q.popleft()
            score = visited[x]

            for nxt in edges[x]:
                if visited[nxt] != -1: continue
                visited[nxt] = visited[x] + 1
                q.append(nxt)
        
        ans[i] = score
    
    a = min(ans[1:])
    print(a, ans.count(a))
    print(*[i for i, x in enumerate(ans) if x == a])