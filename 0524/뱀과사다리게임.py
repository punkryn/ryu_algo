# https://www.acmicpc.net/problem/16928
import sys
from collections import deque
si = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())
    visited = [[False] * 11 for _ in range(11)]
    move = [0] * 101
    for _ in range(n + m):
        a, b = map(int, si().split())
        move[a - 1] = b - 1
    
    q = deque([(0, 0)])
    visited[0][0] = True
    while q:
        number, cost = q.popleft()
        if number == 99:
            print(cost)
            break
        
        for i in range(1, 7):
            nxt_number = number + i
            if nxt_number > 99: continue
            nx, ny = nxt_number // 10, nxt_number % 10
            
            if visited[nx][ny]: continue
            visited[nx][ny] = True

            if move[nxt_number] == 0:
                q.append((nxt_number, cost + 1))
            else:
                nnx = move[nxt_number] // 10
                nny = move[nxt_number] % 10
                if visited[nnx][nny]: continue
                visited[nnx][nny] = True
                q.append((move[nxt_number], cost + 1))