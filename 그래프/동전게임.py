# https://www.acmicpc.net/problem/9079
import sys
from collections import deque
si = sys.stdin.readline

FRONT = (1 << 9) - 1
BACK = 0
compares = [0b000000111, 0b000111000, 0b111000000, 0b001001001, 0b010010010, 0b100100100, 0b100010001, 0b001010100]
if __name__ == '__main__':
    for _ in range(int(si())):
        board = [si().split() for _ in range(3)]
        
        st = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'H':
                    st |= 1 << i * 3 + j
        
        visited = [0] * (1 << 10)
        visited[st] = 1
        q = deque()
        q.append((st, 0))
        
        ans = -1
        while q:
            cur, cnt = q.popleft()

            if cur == BACK or cur == FRONT:
                ans = cnt
                break
            
            for comp in compares:
                nxt = cur ^ comp
                if visited[nxt] != 0:
                    continue
                
                visited[nxt] = 1
                q.append((nxt, cnt + 1))

        print(ans)