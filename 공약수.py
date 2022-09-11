# https://www.acmicpc.net/problem/2436
import sys
import math
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    a, b = mis()
    c = b // a
    
    y = []
    for i in range(1, int(math.sqrt(c)) + 1):
        if c % i == 0:
            y.append(i)
    
    ans = float('inf')
    a_, b_ = 0, 0
    for i in y:
        j = c // i
        if ans > a * i + b * j and math.gcd(a * i, a * j) == a:
            ans = a * i + b * j
            a_, b_ = a * i, a * j
    print(a_, b_)