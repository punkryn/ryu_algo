from collections import deque

def solution(places):
    def bfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited = [[False] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        while q:
            a, b = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == False:
                    if k[nx][ny] == 'O':
                        visited[nx][ny] = True
                        distance[nx][ny] = distance[a][b] + 1
                        q.append((nx, ny))
                    if k[nx][ny] == 'P' and distance[a][b] < 2:
                        return 0
        return 1

    answer = []
    d = 0
    for k in places:
        start = []
        for i in range(len(k)):
            for j in range(5):
                if k[i][j] == 'P':
                    start.append((i, j))
        # start : P의 좌표들(출발지점)
        for x, y in start:
            d = bfs(x, y)
        if not start:
            answer.append(1)
        else:
            answer.append(d)
    return answer