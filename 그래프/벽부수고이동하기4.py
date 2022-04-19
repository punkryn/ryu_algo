# https://www.acmicpc.net/problem/16946
import sys
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, cnt):
    st = [(x, y)]
    visited[x][y] = cnt
    group = 1
    while st:
        x, y = st.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny] or MAP[nx][ny] == '1':
                continue
            
            visited[nx][ny] = cnt
            st.append((nx, ny))
            group += 1
    return group

if __name__ == '__main__':
    n, m = map(int, si().split())
    MAP = [si().strip() for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    group_cnt = {0: 0}
    for i in range(n):
        for j in range(m):
            if visited[i][j] or MAP[i][j] == '1': continue
            cnt += 1
            group_cnt[cnt] = DFS(i, j, cnt)
    
    for i in range(n):
        ans = ''
        for j in range(m):
            if MAP[i][j] == '0':
                ans += '0'
            else:
                tmp = 1
                used = set()
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if not (0 <= ni < n and 0 <= nj < m): continue
                    if visited[ni][nj] not in used:
                        tmp += group_cnt[visited[ni][nj]]
                        used.add(visited[ni][nj])
                ans += str(tmp % 10)
        print(ans)