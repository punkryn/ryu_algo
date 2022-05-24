# https://www.acmicpc.net/problem/2143
from sys import stdin
from collections import defaultdict
si = stdin.readline

if __name__ == '__main__':
    t = int(si())
    n = int(si())
    a = list(map(int, si().split()))
    m = int(si())
    b = list(map(int, si().split()))
    
    ps = [0] * (m + 1)
    for i in range(1, m + 1):
        ps[i] = ps[i - 1] + b[i - 1]
    
    subarr = defaultdict(int)
    for i in range(m):
        for j in range(i, m):
            subarr[ps[j + 1] - ps[i]] += 1
    
    a_ps = [0] * (n + 1)
    for i in range(1, n + 1):
        a_ps[i] = a_ps[i - 1] + a[i - 1]
    
    ans = 0
    for i in range(n):
        for j in range(i, n):
            s = a_ps[j + 1] - a_ps[i]
            ans += subarr.get(t - s, 0)
    print(ans)