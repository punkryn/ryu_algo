# https://www.acmicpc.net/problem/3020
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n, h = mis()
    ob = [int(si()) for _ in range(n)]

    ps = [0] * (h + 2)
    for i in range(n):
        if i % 2:
            ps[h - ob[i] + 1] += 1
            ps[h + 1] -= 1
        else:
            ps[1] += 1
            ps[ob[i] + 1] -= 1
    
    for i in range(1, h + 2):
        ps[i] += ps[i - 1]
    
    ans = min(ps[1: h + 1])
    print(ans, ps[1: h + 1].count(ans))