# https://www.acmicpc.net/problem/14867
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    a, b, c, d = mis()
    
    q = deque([(0, 0, 0)])
    visited = set([(0, 0)])
    ans = -1
    while q:
        x, y, t = q.popleft()
        
        if x == c and y == d:
            ans = t
            break

        for nx, ny in [(a, y), (x, b), (0, y), (x, 0)]:
            if (nx, ny) in visited: continue
            visited.add((nx, ny))
            q.append((nx, ny, t + 1))
        
        # x <- y
        if x + y > a:
            nx, ny = a, x + y - a
        else:
            nx, ny = x + y, 0
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            q.append((nx, ny, t + 1))
        
        # x -> y
        if x + y > b:
            nx, ny = x + y - b, b
        else:
            nx, ny = 0, x + y
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            q.append((nx, ny, t + 1))
    print(ans)