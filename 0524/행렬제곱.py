# https://www.acmicpc.net/problem/10830
from sys import stdin
si = stdin.readline

def mul(m1, m2):
    ret = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            e = 0
            for k in range(n):
                e += m1[i][k] * m2[k][j]
                e %= 1000
            ret[i][j] = e % 1000
    return ret

if __name__ == '__main__':
    n, b = map(int, si().split())
    matrix = [list(map(int, si().split())) for _ in range(n)]
    
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        ans[i][i] = 1
    while b:
        if b & 1:
            ans = mul(ans, matrix)
            b -= 1

        matrix = mul(matrix, matrix)
        b //= 2
    for v in ans:
        print(*v)