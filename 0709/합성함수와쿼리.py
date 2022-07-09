# https://www.acmicpc.net/problem/17435
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    m = int(si())
    f = [0] + list(map(int, si().split()))
    q = int(si())

    nxt = [[0] * 500001 for _ in range(19)]
    for i in range(1, m + 1):
        nxt[0][i] = f[i]
    
    for j in range(1, 19):
        for i in range(1, m + 1):
            nxt[j][i] = nxt[j - 1][nxt[j - 1][i]]

    # for d in nxt[:6]:
    #     print(d[:6])

    for _ in range(q):
        n, x = map(int, si().split())
        for j in range(18, -1, -1):
            if n >= (1 << j):
                n -= 1 << j
                x = nxt[j][x]
        print(x)
