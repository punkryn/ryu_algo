from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution(n, m, image):
    answer = 0
    
    visited = [[False] * m for _ in range(n)]
    print(image)
    print(visited)
    for i in range(n):
        for j in range(m):
            if visited[i][j]: continue
            answer += 1
            q = deque()
            q.append((i, j))
            
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[i]
                    print(nx, ny)
                    if not (0 <= nx < n and 0 <= ny < m) or image[nx][ny] != image[i][j] or visited[nx][ny]:
                        continue
                    
                    visited[nx][ny] = True
                    q.append((nx, ny))
    
    return answer

n = 2
m = 3
images = [[1, 2, 3], [3, 2, 1]]
solution(n, m, images)