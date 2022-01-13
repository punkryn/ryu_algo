# https://www.acmicpc.net/problem/2251

import sys
from collections import deque
si = sys.stdin.readline
visited = [[[False] * 201 for _ in range(201)] for _ in range(201)]

def move(cur, capa, get, give):
    tmp = [cur[0], cur[1], cur[2]]
    if cur[get] + cur[give] <= capa[get]:
        tmp[get] += tmp[give]
        tmp[give] = 0
    else:
        tmp[give] -= capa[get] - tmp[get]
        tmp[get] = capa[get]
    return tmp

def dfs(cur, capa, ans):
    visited[cur[0]][cur[1]][cur[2]] = True
    
    if cur[0] == 0:
        ans.append(cur[2])
    
    for i in range(3):
        for j in range(3):
            if i == j: continue
            nxt = move(cur, capa, j, i)
            if visited[nxt[0]][nxt[1]][nxt[2]]: continue

            dfs(nxt, capa, ans)

def bfs(capa):
    q = deque()
    q.append((0, 0, capa[2]))
    visited[0][0][capa[2]] = True
    ans = []
    while q:
        cur = q.popleft()
        
        if cur[0] == 0:
            ans.append(cur[2])

        for i in range(3):
            for j in range(3):
                if i == j: continue
                nxt = move(cur, capa, j, i)
                if visited[nxt[0]][nxt[1]][nxt[2]]: continue
                visited[nxt[0]][nxt[1]][nxt[2]] = True
                q.append(nxt)
    return sorted(ans)

def main():
    a, b, c = map(int, si().split())
    # ans = bfs([a, b, c])
    ans = []
    dfs([0, 0, c], [a,b,c], ans)
    print(*sorted(ans))

if __name__ == '__main__':
    main()