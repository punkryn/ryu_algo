# https://www.acmicpc.net/problem/21943
import sys
from itertools import permutations as pt
si = sys.stdin.readline

def main():
    n = int(si())
    x = list(map(int, si().split()))
    p, q = map(int, si().split())

    if q == 0:
        print(sum(x))
        return
    elif p == 0:
        ans = 1
        for v in x:
            ans *= v
        print(ans)
        return

    candidate = []
    def go(depth, total, cur, prev):
        if depth == 0:
            if total == n:
                candidate.append(tuple(cur))
            return
        
        for i in range(prev, n - depth + 1):
            if i == 0: continue
            cur.append(i)
            go(depth - 1, total + i, cur, i)
            cur.pop()
    
    go(q + 1, 0, [], 0)

    ans = 0
    for per in pt(x, n):
        for cand in candidate:
            start = 0
            total = 1
            for c in cand:
                total *= sum(per[start:start + c])
                start += c
            ans = max(ans, total)
    print(ans)

if __name__ == '__main__':
    main()