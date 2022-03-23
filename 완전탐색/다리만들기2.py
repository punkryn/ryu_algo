# https://www.acmicpc.net/problem/17472
import sys
from collections import deque
from itertools import combinations
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def main():
    n, m = map(int, si().split())
    MAP = [list(map(int, si().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    islandPosition = [[] for _ in range(7)]
    def bfs(i, j, cnt):
        q = deque()
        q.append((i, j))
        islandPosition[cnt].append((i, j))
        visited[i][j] = cnt
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                    
                if visited[nx][ny] != 0:
                    continue

                if MAP[nx][ny] != 1:
                    continue

                visited[nx][ny] = cnt
                q.append((nx, ny))
                islandPosition[cnt].append((nx, ny))
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 0 or MAP[i][j] != 1:
                continue
            cnt += 1
            bfs(i, j, cnt)
    
    def findParent(parent, a):
        if parent[a] != a:
            parent[a] = findParent(parent, parent[a])
        return parent[a]
    
    def union(parent, a, b):
        a = findParent(parent, a)
        b = findParent(parent, b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    # def go(depth, prev, length):
    #     if depth == 0:
    #         return
        
    #     for i in range(prev + 1, cnt - depth + 2):
    #         print(prev, i)
    #         go(depth - 1, i, length)
    # print(cnt)
    # go(cnt - 1, 1, 0)

    def makeBridge(a, b):
        candidate = int(1e9)
        for pos in islandPosition[a]:
            for i in range(4):
                x, y = pos
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < n and 0 <= ny < m): continue
                if MAP[nx][ny] != 0: continue
                tx, ty = nx, ny
                cnt = 0
                while 0 <= tx < n and 0 <= ty < m:
                    if visited[tx][ty] != 0:
                        if visited[tx][ty] == b:
                            if cnt == 1:
                                break
                            candidate = min(candidate, cnt)
                        break
                    cnt += 1
                    tx += dx[i]
                    ty += dy[i]
        return candidate

    ans = int(1e9)
    for comb in combinations(combinations(list(range(1, cnt + 1)), 2), cnt - 1):
        total = 0
        parent = [i for i in range(cnt + 1)]
        for c in comb:
            ai, bi = c
            if findParent(parent, ai) != findParent(parent, bi):
                union(parent, ai, bi)
            length = makeBridge(ai, bi)
            if length == int(1e9):
                break

            total += length
        else:
            parentCnt = 0
            for i in range(1, cnt + 1):
                if findParent(parent, i) == 1:
                    parentCnt += 1
            if parentCnt == cnt:
                ans = min(ans, total)
    if ans == int(1e9):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
    