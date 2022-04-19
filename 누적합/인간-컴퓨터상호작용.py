# https://www.acmicpc.net/problem/16139
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    s = si().strip()

    ps = [[0] * 26 for _ in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        for j in range(26):
            ps[i][j] += ps[i - 1][j]
        ps[i][ord(s[i - 1]) - ord('a')] += 1

    q = int(si())
    for _ in range(q):
        a, l, r = si().split()
        l = int(l)
        r = int(r)
        print(ps[r + 1][ord(a) - ord('a')] - ps[l][ord(a) - ord('a')])