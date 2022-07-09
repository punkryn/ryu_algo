# https://www.acmicpc.net/problem/1405
import sys
si = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def go(depth, x, y, cur=[]):
    global ans
    if depth == n:
        tmp = 1
        for c in cur:
            if p[c] == 0:
                tmp = 0
                break
            tmp = tmp * p[c] / 100
        ans += tmp
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if visited[nx][ny]: continue
        visited[nx][ny] += 1
        cur.append(i)
        go(depth + 1, nx, ny, cur)
        cur.pop()
        visited[nx][ny] -= 1
        

if __name__ == '__main__':
    n, *p = map(int, si().split())
    ans = 0
    
    visited = [[0] * 30 for _ in range(30)]
    visited[15][15] = 1
    go(0, 15, 15)

    print(f'{ans:.9f}')