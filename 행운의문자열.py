# https://www.acmicpc.net/problem/1342
import sys
from math import factorial
from itertools import permutations
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    s = list(si().strip())
    n = len(s)
    cnt = dict()
    for i in range(n):
        if s[i] not in cnt:
            cnt[s[i]] = 0
        cnt[s[i]] += 1
    
    ans = 0
    for p in permutations(s, n):
        for i in range(n - 1):
            if p[i] == p[i + 1]:
                break
        else:
            ans += 1

    for key in cnt:
        ans //= factorial(cnt[key])
    print(ans)