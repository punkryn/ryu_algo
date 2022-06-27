# https://www.acmicpc.net/problem/17435
import sys
si = sys.stdin.readline

MAX = 500001
MAXD = 19
if __name__ == '__main__':
    m = int(si())
    f = [0] + list(map(int, si().split()))
    q = int(si())
    
    st = [[0] * MAX for _ in range(MAXD)]
    for i in range(1, m + 1):
        st[0][i] = f[i]

    for i in range(1, MAXD):
        for j in range(1, m + 1):
            st[i][j] = st[i - 1][st[i - 1][j]]
    
    for _ in range(q):
        n, x = map(int, si().split())
        for i in range(MAXD - 1, -1, -1):
            tmp = 1 << i
            if n >= tmp:
                n -= tmp
                x = st[i][x]
        print(x)