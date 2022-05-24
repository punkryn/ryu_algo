# https://www.acmicpc.net/problem/2571
from sys import stdin
si = stdin.readline

def isRec(ts, te, bs, bc):
    for i in range(ts, te + 1):
        for j in range(bs, bc + 1):
            if p[i][j] == 0:
                return 0
    return 1

def check(r, c):
    for i in range(1, 101 - r + 1):
        for j in range(1, 101 - c + 1):
            if isRec(i, i + r - 1, j, j + c - 1):
                return True
    return False

if __name__ == '__main__':
    n = int(si())
    p = [[0] * 110 for _ in range(110)]
    for _ in range(1, n + 1):
        a, b = map(int, si().split())
        p[a][b] += 1
        p[a + 10][b + 10] += 1
        p[a][b + 10] -= 1
        p[a + 10][b] -= 1
        
    for i in range(1, 101):
        for j in range(1, 101):
            p[i][j] += p[i - 1][j]
    
    for j in range(1, 101):
        for i in range(1, 101):
            p[i][j] += p[i][j - 1]
    
    # for i in range(21):
    #     for j in range(21):
    #         print(p[i][j], end=' ')
    #     print()

    ans = 0
    for i in range(1, 101):
        for j in range(1, 101):
            if check(i, j):
                ans = max(ans, i * j)

    print(ans)