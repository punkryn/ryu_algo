# https://www.acmicpc.net/problem/1030
import sys
import math
si = sys.stdin.readline

def shape(rs, re, cs, ce, cur):
    if rs == re:
        return

    l = re - rs + 1
    cnt = int(math.log(l, n))
    cen = k * (n ** (cnt - 1))
    prev1 = 0
    for i in range(n):
        prev2 = 0
        for j in range(n):
            shape(prev1, prev1 + l // n - 1, prev2, prev2 + l // n - 1, cur)
            prev2 += l // n
        prev1 += l // n
    
    padding = (l - cen) // 2
    for i in range(rs + padding, rs + padding + cen):
        for j in range(cs + padding, cs + padding + cen):
            cur[i][j] = 1

def calc(rs, re, cs, ce, cur):
    for dd in cur:
        print(dd)
    l = re - rs + 1
    for i in range(max(rs, r1), min(re, r2) + 1):
        for j in range(max(cs, c1), min(ce, c2) + 1):
            print(i, j, i % l, j % l, row_idx[i])
            ans[row_idx[i]] += str(cur[i % l][j % l])

def dnq(rs, re, cs, ce):
    # in range
    if (r1 <= rs <= r2 or r1 <= re <= r2) and (c1 <= cs <= c2 or c1 <= ce <= c2):
        tmp = re - rs + 1
        cur = [[0] * tmp for _ in range(tmp)]
        shape(0, tmp - 1, 0, tmp - 1, cur)
        calc(rs, re, cs, ce, cur)
        return

    # out range
    if not ((rs <= r1 <= re or rs <= r2 <= re) and (cs <= c1 <= ce or cs <= c2 <= ce)):
        return
    
    # limit
    if rs == re:
        return
    
    l = (re - rs + 1) // n
    prev1 = 0
    for i in range(n):
        prev2 = 0
        for j in range(n):
            dnq(prev1, prev1 + l - 1, prev2, prev2 + l - 1)
            prev2 += l
        prev1 +=l

if __name__ == '__main__':
    s, n, k, r1, r2, c1, c2 = map(int, si().split())
    length = n ** s
    center = k * (n ** (s - 1))
    row_idx = {i: i - r1 for i in range(r1, r2 + 1)}
    ans = [''] * (r2 - r1 + 1)
    dnq(0, length - 1, 0, length - 1)
    print('\n'.join(ans))