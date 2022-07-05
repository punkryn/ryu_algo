# https://www.acmicpc.net/problem/2448
import sys
si = sys.stdin.readline

def draw(l, r, t, b):
    board[t][(l + r) // 2 - 1] = '*'
    board[t + 1][l + 1] = '*'
    board[t + 1][r - 3] = '*'
    for i in range(l, r - 1):
        board[t + 2][i] = '*'

def go(l, r, t, b):
    if r - l <= 5 or b - t <= 3:
        draw(l, r, t, b)
        return
    
    go(l + (r - l) // 4, r - (r - l) // 4, t, (t + b) // 2)
    go(l, (l + r) // 2, (t + b) // 2, b)
    go((l + r) // 2, r, (t + b) // 2, b)

if __name__ == '__main__':
    n = int(si())
    l = n // 3
    w = 6 * l
    board = [[' '] * w for _ in range(n)]
    go(0, w, 0, n)
    for b in board:
        print(''.join(b)) 