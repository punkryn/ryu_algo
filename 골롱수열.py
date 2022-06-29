# https://www.acmicpc.net/problem/2038
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    p = q = 1
    s = [0] * int(1e7)
    s[1] = 1
    while q < n:
        p += 1
        s[p] = 1 + s[p - s[s[p - 1]]]
        q += s[p]
    print(p)