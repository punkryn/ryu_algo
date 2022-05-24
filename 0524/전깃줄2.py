# https://www.acmicpc.net/problem/2568
from sys import stdin
from bisect import bisect_left
si = stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = []
    dic = dict()
    for _ in range(n):
        x, y = map(int, si().split())
        a.append([x, y])
        dic[x] = y
    a.sort(key=lambda x: x[0])

    dp = []
    ans = []
    for _, x in a:
        try:
            if dp[-1] < x:
                dp.append(x)
                ans.append(len(dp))
            else:
                idx = bisect_left(dp, x)
                dp[idx] = x
                ans.append(idx + 1)
        except:
            dp.append(x)
            ans.append(len(dp))
    print(n - len(dp))
    
    j = len(dp)
    visited = []
    for i in range(n - 1, -1, -1):
        if ans[i] == j:
            j -= 1
            visited.append(a[i][0])

    for v in visited:
        del dic[v]
    
    for v in sorted(dic):
        print(v)