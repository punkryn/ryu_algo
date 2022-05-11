# https://www.acmicpc.net/problem/1780
from sys import stdin
si = stdin.readline

def check(rs, re, cs, ce):
    cnt_1, cnt0, cnt1 = 0, 0, 0
    for i in range(rs, re + 1):
        for j in range(cs, ce + 1):
            if matrix[i][j] == -1:
                cnt_1 += 1
            elif matrix[i][j] == 0:
                cnt0 += 1
            else:
                cnt1 += 1
    
    if cnt_1 == 0 and cnt0 == 0:
        return 1
    elif cnt_1 == 0 and cnt1 == 0:
        return 0
    elif cnt0 == 0 and cnt1 == 0:
        return -1
    else:
        return 2

def dnq(rs, re, cs, ce):
    global x, y, z
    op = check(rs, re, cs, ce)
    
    if op == -1:
        x += 1
        return
    elif op == 0:
        y += 1
        return
    elif op == 1:
        z += 1
        return
    
    u = (re - rs + 1) // 3
    for row in [rs, rs + u, rs + u + u]:
        for col in [cs, cs + u, cs + u + u]:
            dnq(row, row + u - 1, col, col + u - 1)

if __name__ == '__main__':
    n = int(si())
    matrix = [list(map(int, si().split())) for _ in range(n)]
    x, y, z = 0, 0, 0
    dnq(0, n - 1, 0, n - 1)
    print(x)
    print(y)
    print(z)