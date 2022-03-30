# https://www.acmicpc.net/problem/20167
import sys
si = sys.stdin.readline

def go(depth, prev, cur):
    global ans
    if depth == 0:
        for i in range(len(cur) - 1):
            for j in range(i + 1, len(cur)):
                if cur[i][1] >= cur[j][0]:
                    return
        total = 0
        for c in cur:
            total += c[2]
        ans = max(ans, total)
        return
    
    for i in range(prev + 1, length - depth + 1):
        cur.append(cand[i])
        go(depth - 1, i, cur)
        cur.pop()
        go(depth - 1, i, cur)

if __name__ == '__main__':
    n, k = map(int, si().split())
    a = list(map(int, si().split()))
    
    r = -1
    total = 0
    cand = []
    for i in range(n):
        flag = False
        while r + 1 < n and total < k:
            r += 1
            total += a[r]

        if total >= k:
            cand.append((i, r, total - k))
        total -= a[i]
    
    length = len(cand)
    ans = 0
    go(length, -1, [])
    print(ans)