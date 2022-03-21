# https://www.acmicpc.net/problem/10986

import sys
si = sys.stdin.readline

def main():
    n, m = map(int, si().split())
    a = list(map(int, si().split()))
    # a = [x % m for x in a]
    ps = [0] * (n + 1)
    for i in range(1, n + 1):
        ps[i] = ps[i-1] + a[i-1]

    dic_ = {}
    for i in range(m):
        dic_[i] = 0

    for i in range(1, n + 1):
        ps[i] %= m
        dic_[ps[i]] += 1
    dic_[0] += 1
    ans = 0
    for key in dic_:
        k = dic_[key]
        ans += k * (k - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()