# https://www.acmicpc.net/problem/2900
import sys
import math
from collections import defaultdict
si = sys.stdin.readline

def main():
    n, k = map(int, si().split())
    x = list(map(int, si().split()))
    q = int(si())
    checks = [list(map(int, si().split())) for _ in range(q)]

    ps = [0] * (n + 1)
    origin = [0] * (n + 1)
    arr = defaultdict(int)
    for xi in x:
        arr[xi] += 1
    
    for key in arr:
        for j in range(key, n, key):
            origin[j] += arr[key]
    ps[0] = k
    for i in range(1, n):
        ps[i] = origin[i] + ps[i - 1]
    
    for query in checks:
        l, r = query
        ans = ps[r] - (ps[l - 1] if l > 0 else 0)
        print(ans)

if __name__ == '__main__':
    main()