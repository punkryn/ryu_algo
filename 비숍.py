# https://www.acmicpc.net/problem/1799
from sys import stdin
si = stdin.readline

def check(row, col):
    r = row
    left = col
    while r - 1 >= 0:
        r -= 1
        if left - 1 >= 0:
            left -= 1
            if visited[r] & (1 << left):
                return False
        else:
            break
    
    r = row
    right = col
    while r - 1 >= 0:
        r -= 1
        if right + 1 < n:
            right += 1
            if visited[r] & (1 << right):
                return False
        else:
            break
    return True

def go(depth, cnt, col):
    global ans, ans2
    if col >= n:
        col = (col + 1) % 2
        depth += 1

    if depth == n:
        if flag:
            ans = max(ans, cnt)
        else:
            ans2 = max(ans2, cnt)
        return
    
    go(depth, cnt, col + 2)
    if board[depth][col] == 1 and check(depth, col):
        tmp = visited[depth]
        visited[depth] |= (1 << col)
        go(depth, cnt + 1, col + 2)
        visited[depth] = tmp

if __name__ == '__main__':
    n = int(si())
    board = [list(map(int, si().split())) for _ in range(n)]
    
    visited = [0] * n
    flag = True
    ans = 0
    go(0, 0, 0)
    flag = False
    ans2 = 0
    visited = [0] * n
    go(0, 0, 1)
    print(ans + ans2)