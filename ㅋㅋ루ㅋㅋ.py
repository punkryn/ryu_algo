# https://www.acmicpc.net/problem/20442
from sys import stdin
si = stdin.readline

if __name__ == '__main__':
    s = si().strip()
    n = len(s)
    lk = []
    rk = []
    cnt = 0
    for i in range(n):
        if s[i] == 'K':
            cnt += 1
        else:
            lk.append(cnt)
    
    cnt = 0
    for i in range(n - 1, -1, -1):
        if s[i] == 'K':
            cnt += 1
        else:
            rk.append(cnt)
    rk.reverse()

    l, r = 0, len(rk) - 1
    ans = 0
    while l <= r:
        ans = max(ans, r - l + 1 + min(lk[l], rk[r]) * 2)

        if lk[l] < rk[r]:
            l += 1
        else:
            r -= 1
        
    print(ans)