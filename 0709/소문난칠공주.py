# https://www.acmicpc.net/problem/1941
from sys import stdin
from itertools import combinations
from collections import deque
si = stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
        
def bfs(x, y, visited, cand):
    q = deque([(x, y)])
    visited.add((x, y))
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < 5 and 0 <= ny < 5):
                continue
            if (nx, ny) in visited:
                continue
            if (nx, ny) not in cand: continue
            visited.add((nx, ny))
            q.append((nx, ny))

def isConnected(cand):
    visited = set()
    cnt = 0
    for x, y in cand:
        if (x, y) in visited: continue
        cnt += 1
        bfs(x, y, visited, cand)
    return cnt == 1

if __name__ == '__main__':
    matrix = [si().strip() for _ in range(5)]
    ans = 0
    for comb in combinations(range(25), 7):
        cnt = 0
        cand = set()
        for num in comb:
            x = num // 5
            y = num % 5
            cand.add((x, y))
            if matrix[x][y] == 'Y':
                cnt += 1
        
        if cnt >= 4: continue
        if isConnected(cand):
            ans += 1
    
    print(ans)