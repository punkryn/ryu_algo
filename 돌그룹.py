# https://www.acmicpc.net/problem/12886
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def remain(x, y):
    return [c for c in [0, 1, 2] if c != x and c != y]

if __name__ == '__main__':
    a, b, c = mis()
    
    s = sorted([a, b, c])
    q = deque([tuple(s)])
    visited = set(tuple(s))

    ans = 0
    while q:
        cur = q.popleft()

        if cur[0] == cur[1] and cur[1] == cur[2]:
            ans = 1
            break
        
        for i in range(2):
            for j in range(1, 3):
                if cur[i] == cur[j]: continue
                
                x, y = min(cur[i], cur[j]), max(cur[i], cur[j])
                
                nx = x + x
                ny = y - x
                
                nxt = tuple(sorted([cur[remain(i, j)[0]], nx, ny]))
                if nxt  in visited:
                    continue

                visited.add(nxt)
                q.append(nxt)

    print(ans)