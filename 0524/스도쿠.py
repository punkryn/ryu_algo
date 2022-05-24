# https://www.acmicpc.net/problem/2580
import sys
si = sys.stdin.readline

def row_check(x, n):
    return n not in board[x]

def col_check(y, n):
    for i in range(9):
        if board[i][y] == n:
            return False
    return True

def rec_check(x, y, n):
    rs = x // 3
    cs = y // 3 
    for i in range(rs * 3, rs * 3 + 3):
        for j in range(cs * 3, cs * 3 + 3):
            if board[i][j] == n:
                return False
    return True

def go(depth):
    if depth == len(pos):
        for r in board:
            # print(*r)
            print(''.join(map(str, r)))
        exit()
    
    x, y = pos[depth]
    for i in range(1, 10):
        if row_check(x, i) and col_check(y, i) and rec_check(x, y, i):
            board[x][y] = i
            go(depth + 1)
            board[x][y] = 0

if __name__ == '__main__':
    # board = [list(map(int, si().split())) for _ in range(9)]
    board = [[int(n) for n in si().strip()] for _ in range(9)]

    pos = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
    
    go(0)

    # for r in board:
    #     print(*r)