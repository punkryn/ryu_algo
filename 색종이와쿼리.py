# https://www.acmicpc.net/problem/18246
import sys
si = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

MAX_LEN = 1510

def init():
    for i in range(MAX_LEN):
        for j in range(MAX_LEN):
            seg[i + MAX_LEN][j + MAX_LEN] = ps[i][j]
    
    for i in range(MAX_LEN, MAX_LEN * 2):
        for j in range(MAX_LEN - 1, 0, -1):
            seg[i][j] = max(seg[i][j << 1], seg[i][j<<1|1])
    
    for i in range(MAX_LEN - 1, 0, -1):
        for j in range(1, MAX_LEN * 2):
            seg[i][j] = max(seg[i << 1][j], seg[i<<1|1][j])

def query1D(x, y1, y2):
    ret = 0
    y1 += MAX_LEN
    y2 += MAX_LEN + 1
    while y1 < y2:
        if y1 & 1:
            ret = max(ret, seg[x][y1])
            y1 += 1
        if y2 & 1:
            y2 -= 1
            ret = max(ret, seg[x][y2])
        y1 >>= 1
        y2 >>= 1
    return ret

def query(x1, y1, x2, y2):
    ret = 0
    x1 += MAX_LEN
    x2 += MAX_LEN + 1
    while x1 < x2:
        if x1 & 1:
            ret = max(ret, query1D(x1, y1, y2))
            x1 += 1
        if x2 & 1:
            x2 -= 1
            ret = max(ret, query1D(x2, y1, y2))
        x1 >>= 1
        x2 >>= 1
    return ret

if __name__ == '__main__':
    n, m = map(int, si().split())
    ps = [[0] * MAX_LEN for _ in range(MAX_LEN)]
    for _ in range(n):
        y1, x1, y2, x2 = map(int, si().split())
        ps[y1][x1] += 1
        ps[y1][x2] -= 1
        ps[y2][x2] += 1
        ps[y2][x1] -= 1

    
    for i in range(MAX_LEN):
        for j in range(1, MAX_LEN):
            ps[i][j] += ps[i][j - 1]
    
    for j in range(MAX_LEN):
        for i in range(1, MAX_LEN):
            ps[i][j] += ps[i - 1][j]
    
    h = 1
    while h < MAX_LEN:
        h <<= 1
    seg = [[0] * (h * 2) for _ in range(h * 2)]
    init()

    for _ in range(m):
        y1, x1, y2, x2 = map(int, si().split())
        print(query(y1, x1, y2 - 1, x2 - 1))