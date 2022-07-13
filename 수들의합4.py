# https://www.acmicpc.net/problem/2015
import sys
from collections import defaultdict
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n, k = mis()
    a = list(mis())
    ans = 0
    ps = [0] * (n + 1)
    for i in range(1, n + 1):
        ps[i] = ps[i - 1] + a[i - 1]
    
    v = defaultdict(int)
    for i in range(1, n + 1):
        if ps[i] == k:
            ans += 1
        
        ans += v.get(ps[i] - k, 0)
        v[ps[i]] += 1
    print(ans)