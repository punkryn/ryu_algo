# https://www.acmicpc.net/problem/4963
import sys
sys.setrecursionlimit(100000)
si = sys.stdin.readline
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
def main():
    while True:
        w, h = map(int, si().split())
        if w == 0 and h == 0: break
        MAP = [list(map(int, si().split())) for _ in range(h)]
        visited = [[0] * w for _ in range(h)]

        def dfs(x, y):
            visited[x][y] = 1
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if visited[nx][ny] != 0: continue
                    if MAP[nx][ny] == 0: continue
                    dfs(nx, ny)

        ans = 0
        for i in range(h):
            for j in range(w):
                if MAP[i][j] == 0: continue
                if visited[i][j] != 0: continue
                dfs(i, j)
                ans += 1
        print(ans)

if __name__ == '__main__':
    main()