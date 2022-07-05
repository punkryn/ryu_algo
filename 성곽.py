# https://www.acmicpc.net/problem/2234
import sys
from collections import deque
si = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(x, y, num):
    q = deque([(x, y)])
    visited[x][y] = num
    room_cnt = 0
    while q:
        x, y = q.popleft()
        room_cnt += 1
        
        for nx, ny in graph[x][y]:
            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny] != -1:
                continue
            visited[nx][ny] = num
            q.append((nx, ny))
    return room_cnt

if __name__ == '__main__':
    m, n = map(int, si().split())
    info = [list(map(int, si().split())) for _ in range(n)]
    graph = [[[] for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            bits = info[i][j]
            for k in range(4):
                if (1 << k) & bits: continue
                nx = i + dx[k]
                ny = j + dy[k]
                graph[i][j].append((nx, ny))
    
    visited = [[-1] * m for _ in range(n)]
    num = 0
    cnt = []
    for i in range(n):
        for j in range(m):
            if visited[i][j] != -1: continue
            cnt.append(bfs(i, j, num))
            num += 1
    
    print(num)
    print(max(cnt))

    adj = [set() for _ in range(num)]
    for i in range(n):
        for j in range(m):
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if not (0 <= ni < n and 0 <= nj < m): continue
                if visited[i][j] != visited[ni][nj]:
                    adj[visited[i][j]].add(visited[ni][nj])

    ans = 0
    for i in range(num):
        for j in adj[i]:
            ans = max(ans, cnt[i] + cnt[j])
    print(ans)