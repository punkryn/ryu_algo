# https://www.acmicpc.net/problem/3184
import sys
sys.setrecursionlimit(100000)
si = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def main():
    r, c = map(int, si().split())
    garden = [si().strip() for _ in range(r)]
    visited = [[0] * c for _ in range(r)]

    def dfs(x, y, cnt):
        visited[x][y] = cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] != 0: continue
                if garden[nx][ny] == '#': continue
                dfs(nx, ny, cnt)
    
    cnt = 1
    for i in range(r):
        for j in range(c):
            if visited[i][j] != 0: continue
            if garden[i][j] == '#': continue
            dfs(i, j, cnt)
            cnt += 1

    sheep_total = 0
    wolf_total = 0
    for cnt_ in range(1, cnt):
        sheep = 0
        wolf = 0
        for i in range(r):
            for j in range(c):
                if visited[i][j] == cnt_:
                    if garden[i][j] == 'o':
                        sheep += 1
                    elif garden[i][j] == 'v':
                        wolf += 1
        
        if sheep > wolf:
            sheep_total += sheep
        else:
            wolf_total += wolf
    
    print(sheep_total, wolf_total)

if __name__ == '__main__':
    main()