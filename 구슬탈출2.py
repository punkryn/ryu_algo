# https://www.acmicpc.net/problem/13460
from sys import stdin
from collections import deque
si = stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def red_move(d, rx, ry, bx, by):
    nrx = rx + dx[d]
    nry = ry + dy[d]
    while 0 <= nrx < n and 0 <= nry < m:
        if board[nrx][nry] == '#':
            return False, (nrx - dx[d], nry - dy[d])
        elif board[nrx][nry] == 'O':
            return True, (0, 0)
        elif nrx == bx and nry == by:
            return False, (nrx - dx[d], nry - dy[d])
        
        nrx += dx[d]
        nry += dy[d]
    
    return False, (rx, ry)


def blue_move(d, bx, by, rx, ry):
    nbx = bx + dx[d]
    nby = by + dy[d]
    while 0 <= nbx < n and 0 <= nby < m:
        if board[nbx][nby] == '#':
            return False, (nbx - dx[d], nby - dy[d])
        elif board[nbx][nby] == 'O':
            return True, (0, 0)
        elif nbx == rx and nby == ry:
            return False, (nbx - dx[d], nby - dy[d])
        
        nbx += dx[d]
        nby += dy[d]
    
    return False, (bx, by)

def move(d, rx, ry, bx, by):
    if d == 0 and ry == by:
        if rx > bx:
            blue_flag, (nbx, nby) = blue_move(d, bx, by, rx, ry)
            red_flag, (nrx, nry) = red_move(d, rx, ry, nbx, nby)
        else:
            red_flag, (nrx, nry) = red_move(d, rx, ry, bx, by)
            blue_flag, (nbx, nby) = blue_move(d, bx, by, nrx, nry)
    elif d == 1 and rx == bx:
        if ry < by:
            blue_flag, (nbx, nby) = blue_move(d, bx, by, rx, ry)
            red_flag, (nrx, nry) = red_move(d, rx, ry, nbx, nby)
        else:
            red_flag, (nrx, nry) = red_move(d, rx, ry, bx, by)
            blue_flag, (nbx, nby) = blue_move(d, bx, by, nrx, nry)
    elif d == 2 and ry == by:
        if rx < bx:
            blue_flag, (nbx, nby) = blue_move(d, bx, by, rx, ry)
            red_flag, (nrx, nry) = red_move(d, rx, ry, nbx, nby)
        else:
            red_flag, (nrx, nry) = red_move(d, rx, ry, bx, by)
            blue_flag, (nbx, nby) = blue_move(d, bx, by, nrx, nry)
    elif d == 3 and rx == bx:
        if ry > by:
            blue_flag, (nbx, nby) = blue_move(d, bx, by, rx, ry)
            red_flag, (nrx, nry) = red_move(d, rx, ry, nbx, nby)
        else:
            red_flag, (nrx, nry) = red_move(d, rx, ry, bx, by)
            blue_flag, (nbx, nby) = blue_move(d, bx, by, nrx, nry)
    else:
        red_flag, (nrx, nry) = red_move(d, rx, ry, bx, by)
        blue_flag, (nbx, nby) = blue_move(d, bx, by, nrx, nry)
    
    if blue_flag:
        return False, (-1, -1, -1, -1)
    
    if red_flag:
        return True, (0, 0, 0, 0)
    
    return True, (nrx, nry, nbx, nby)

if __name__ == '__main__':
    n, m = map(int, si().split())
    board = [si().strip() for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                red = (i, j)
            elif board[i][j] == 'B':
                blue = (i, j)
    
    q = deque([(red[0], red[1], blue[0], blue[1], 0)])
    visited = set([(red[0], red[1], blue[0], blue[1])])
    ans = -1
    while q:
        rx, ry, bx, by, cnt = q.popleft()

        if cnt >= 10:
            ans = -1
            break

        for i in range(4):
            flag, nxt_state = move(i, rx, ry, bx, by)
            if not flag or nxt_state in visited: continue
            if sum(nxt_state) == 0:
                print(cnt + 1)
                exit()
            visited.add(nxt_state)
            q.append((*nxt_state, cnt + 1))
    print(ans)