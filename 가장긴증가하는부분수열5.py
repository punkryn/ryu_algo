# https://www.acmicpc.net/problem/14003
from sys import stdin
from bisect import bisect_left
si = stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = list(map(int, si().split()))
    dp = [a[0]]
    ans = [1]
    for i in range(1, n):
        if dp[-1] < a[i]:
            dp.append(a[i])
            ans.append(len(dp))
        else:
            idx = bisect_left(dp, a[i])
            dp[idx] = a[i]
            ans.append(idx + 1)
            
    print(len(dp))
    j = len(dp)
    v = []
    for i in range(n - 1, -1, -1):
        if ans[i] == j:
            j -= 1
            v.append(a[i])
    print(*v[::-1])