# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(100000)
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(ground, visited, x, y, m, n):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if visited[nx][ny] != 0: continue
            if ground[nx][ny] != 1: continue
            dfs(ground, visited, nx, ny, m, n)

def main():
    t = int(si())
    for _ in range(t):
        m, n, k = map(int, si().split())
        pos = [list(map(int, si().split())) for _ in range(k)]
        ground = [[0] * n for _ in range(m)]
        for p in pos:
            ground[p[0]][p[1]] = 1
        visited = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if ground[i][j] == 1 and visited[i][j] == 0:
                    dfs(ground, visited, i, j, m, n)
                    ans += 1
        print(ans)

if __name__ == '__main__':
    main()