# https://www.acmicpc.net/problem/2412
import sys
from collections import deque
si = sys.stdin.readline

d = [-2, -1, 0, 1, 2]

if __name__ == '__main__':
    n, t = map(int, si().split())
    coord = set(tuple(map(int, si().split())) for _ in range(n))
    
    q = deque([(0, 0, 0)])
    visited = set([(0, 0)])
    ans = -1
    while q:
        x, y, cnt = q.popleft()

        if y == t:
            ans = cnt
            break

        for i in range(5):
            nx = x + d[i]
            for j in range(5):
                if d[i] == 0 and d[j] == 0: continue
                ny = y + d[j]
                if nx < 0 or ny < 0: continue
                if (nx, ny) in visited: continue
                if (nx, ny) not in coord: continue
                q.append((nx, ny, cnt + 1))
                visited.add((nx, ny))
    print(ans)