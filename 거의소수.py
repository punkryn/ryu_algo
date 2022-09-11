# https://www.acmicpc.net/problem/1456
import sys
from math import sqrt, log, ceil, floor
si = sys.stdin.readline
mis = lambda: map(int, si().split())


if __name__ == '__main__':
    a, b = mis()
    
    q = int((sqrt(1e7)))
    prime = set([i for i in range(2, q + 1)])
    
    for i in range(2, q + 1):
        for j in range(i, q // i + 1):
            if i * j in prime:
                prime.remove(i * j)
    
    ans = 0
    for p in prime:
        n = ceil(log(a, p))
        m = floor(log(b, p))
        if m <= 1:
            break

        ans += m - (n if n >= 2 else 2) + 1

    print(ans)