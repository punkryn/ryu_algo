# https://www.acmicpc.net/problem/3117
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, k, m = map(int, si().split())
    f = list(map(int, si().split()))
    r = [0] + list(map(int, si().split()))

    st = [[0] * (k + 1) for _ in range(30)]
    st[0] = r
    
    for i in range(1, 30):
        for j in range(1, k + 1):
            st[i][j] = st[i - 1][st[i - 1][j]]
    
    for i in f:
        i_ = st[0][i]
        m_ = m - 2
        for j in range(29, -1, -1):
            tmp = 1 << j
            if m_ >= tmp:
                m_ -= tmp
                i_ = st[j][i_]
        print(i_, end=' ')