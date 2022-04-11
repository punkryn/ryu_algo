# https://www.acmicpc.net/problem/12015
import sys
from bisect import bisect_left as bs
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = list(map(int, si().split()))
    dp = [a[0]]

    for i in range(1, n):
        idx = bs(dp, a[i])
        if idx >= len(dp):
            dp.append(a[i])
        else:
            dp[idx] = a[i]
    print(len(dp))