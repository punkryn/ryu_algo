# https://www.acmicpc.net/problem/12850
from sys import stdin
si = stdin.readline
MOD = 1000000007
def mul(m1, m2):
    ret = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            e = 0
            for k in range(8):
                e += m1[i][k] * m2[k][j]
                e %= MOD
            ret[i][j] = e % MOD
    return ret

if __name__ == '__main__':
    D = int(si())

    matrix = [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0]
    ]

    ans = [[0] * 8 for _ in range(8)]
    for i in range(8):
        ans[i][i] = 1
    
    while D:
        if D & 1:
            ans = mul(ans, matrix)
            D -= 1
        matrix = mul(matrix, matrix)
        D //= 2
    print(ans[0][0])