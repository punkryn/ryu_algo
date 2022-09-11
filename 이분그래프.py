# https://www.acmicpc.net/problem/1707
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def bfs(x):
    q = deque([(x, 1)])
    visited[x] = True
    flag[x] = 1
    while q:
        cur, f = q.popleft()

        for nxt in graph[cur]:
            if f == 1:
                if flag[nxt] == 1:
                    return False
            elif f == 2:
                if flag[nxt] == 2:
                    return False

            if visited[nxt]: continue
            visited[nxt] = True
            if f == 1:
                flag[nxt] = 2
                q.append((nxt, 2))
            elif f == 2:
                flag[nxt] = 1
                q.append((nxt, 1))
    return True

                
if __name__ == '__main__':
    for _ in range(int(si())):
        v, e = mis()
        graph = [[] for _ in range(v + 1)]
        for _ in range(e):
            a, b = mis()
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * (v + 1)
        flag = [0] * (v + 1)
        for i in range(1, v + 1):
            if visited[i]: continue
            if not bfs(i):
                print('NO')
                break
        else:
            print('YES')