import sys
from collections import deque
si = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())

    q = deque()
    q.append((n, 0))
    visited = set()
    visited.add(n)

    while q:
        cur, cnt = q.popleft()

        nxt1 = cur * 2
        if nxt1 > m:
            continue
        if nxt1 == m:
            print(cnt + 2)
            exit()
        if nxt1 not in visited:
            visited.add(nxt1)
            q.append((nxt1, cnt + 1))
        
        nxt2 = cur * 10 + 1
        if nxt2 > m:
            continue
        if nxt2 == m:
            print(cnt + 2)
            exit()
        if nxt2 not in visited:
            visited.add(nxt2)
            q.append((nxt2, cnt + 1))
    
    print(-1)