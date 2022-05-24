# https://www.acmicpc.net/problem/15566
import sys
from collections import deque
si = sys.stdin.readline

def BFS(x, v, l):
    v[x] = 1
    q = deque([x])
    while q:
        cur_ = q.popleft()

        for nxt, subject in graph[cur_]:
            if v[nxt]: continue
            if interest[l[cur_] - 1][subject - 1] != interest[l[nxt] - 1][subject - 1]:
                return False
            v[nxt] = 1
            q.append(nxt)
    return True

def go(depth):
    global flag
    if depth == n:
        if 0 in cur[1:] or 0 in visited[1:]:
            return
        v = [0] * (n + 1)
        for i in range(1, n + 1):
            if v[i]: continue
            if not BFS(i, v, cur):
                break 
        else:
            flag = True
            print('YES')
            print(*cur[1:])
            exit()
        return
    
    for p in pri[depth]:
        if p in visited:
            continue
        visited[depth + 1] = p
        cur[p] = depth + 1
        go(depth + 1)
        cur[0] = 0
        visited[depth + 1] = 0

if __name__ == '__main__':
    n, m = map(int, si().split())
    interest = [list(map(int, si().split())) for _ in range(n)]
    pri = [list(map(int, si().split())) for _ in range(n)]
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, t = map(int, si().split())
        graph[a].append((b, t))
        graph[b].append((a, t))
    
    visited = [0] * (n + 1)
    cur = [0] * (n + 1)
    flag = False
    go(0)
    print('NO')