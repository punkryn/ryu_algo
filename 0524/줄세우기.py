# https://www.acmicpc.net/problem/2631
import sys
from bisect import bisect_left
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = [int(si()) for _ in range(n)]

    dp = [a[0]]
    for i in range(1, n):
        if dp[-1] < a[i]:
            dp.append(a[i])
        else:
            dp[bisect_left(dp, a[i])] = a[i]
    
    print(n - len(dp))