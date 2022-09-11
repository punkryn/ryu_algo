# https://www.acmicpc.net/problem/2824
import sys
import math
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())
    a = list(mis())
    m = int(si())
    b = list(mis())

    ans = 1
    
    for i in b:
        for j in range(n):
            gcd = math.gcd(a[j], i)
            a[j] //= gcd
            i //= gcd
            ans *= gcd
    
    ans = str(ans)
    length = len(ans)
    print(ans if length <= 9 else ans[length - 9:])