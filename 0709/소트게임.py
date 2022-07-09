# https://www.acmicpc.net/problem/1327
import sys
from collections import deque
si = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, si().split())
    arr = tuple(map(int, si().split()))
    q = deque([(arr, 0, ())])
    visited = set()
    visited.add(arr)
    ans = tuple(i for i in range(1, n + 1))
    while q:
        cur, cnt, prev = q.popleft()
        if cur == ans:
            print(cnt)
            exit()
        
        for i in range(n - k + 1):
            l = list(cur)
            if i > 0:
                nxt = tuple(l[:i] + l[i + k - 1: i - 1: -1] + l[i + k:])
            else:
                nxt = tuple(l[:i] + l[i + k - 1:: -1] + l[i + k:])
            if nxt in visited: continue
            visited.add(nxt)
            q.append([nxt, cnt + 1, cur])
    print(-1)