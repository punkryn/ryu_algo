# https://www.acmicpc.net/problem/20955
import sys
from collections import deque
si = sys.stdin.readline

def BFS(x):
    q = deque()
    q.append(x)
    visited[x] = True
    cnt = 0
    while q:
        cur = q.popleft()

        for nxt in tree[cur]:
            if visited[nxt]: continue
            visited[nxt] = True
            q.append(nxt)
            cnt += 1
    return cnt

if __name__ == '__main__':
    n, m = map(int, si().split())
    parent = [i for i in range(n + 1)]
    tree = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, si().split())
        tree[a].append(b)
        tree[b].append(a)
    
    visited = [False] * (n + 1)
    edge = 0
    ans = 0
    for i in range(1, n + 1):
        if visited[i]: continue
        ans += 1
        edge += BFS(i)
    print(ans - 1 + m - edge)