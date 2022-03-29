# https://www.acmicpc.net/problem/18232
import sys
from collections import deque
si = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())
    s, e = map(int, si().split())
    points = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, si().split())
        points[x].append(y)
        points[y].append(x)
    
    q = deque()
    q.append((s, 0))
    visited = [0] * (n + 1)
    visited[s] = 1
    ans = 0
    while q:
        cur, time = q.popleft()

        if cur == e:
            ans = time

        for nxt in points[cur]:
            if visited[nxt] != 0:
                continue

            visited[nxt] = 1
            q.append((nxt, time + 1))
        
        if cur - 1 >= 1 and visited[cur - 1] == 0:
            visited[cur - 1] = 1
            q.append((cur - 1, time + 1))
        
        if cur + 1 <= n and visited[cur + 1] == 0:
            visited[cur + 1] = 1
            q.append((cur + 1, time + 1))
            
    print(ans)