# https://www.acmicpc.net/problem/20665
from sys import stdin
si = stdin.readline

def dnq(l, r):
    global num
    if l == r - 1:
        return
    
    mid = (l + r) // 2
    seat[num] = mid
    num += 1
    dnq(l, mid)
    dnq(mid, r)

if __name__ == '__main__':
    n, t, p = map(int, si().split())
    timestamp = [[-1] * (60 * 21 + 1) for _ in range(n + 1)]
    order = []
    for _ in range(t):
        start, end = si().split()
        start = int(start[:2]) * 60 + int(start[2:])
        end = int(end[:2]) * 60 + int(end[2:])
        order.append((start, end, end - start))
    order.sort(key=lambda x: (x[0], x[2]))
    
    seat = [0] * (n + 1)
    seat[1] = 1
    if n >= 2:
        seat[2] = n
    if n >= 3:
        num = 3
        dnq(1, n)
    for i in range(len(order)):
        s, e, _ = order[i]
        cnt = 1
        for j in range(i):
            s_, e_, _ = order[j]
            if s < e_:
                cnt += 1
        for j in range(s, e):
            timestamp[seat[cnt]][j] = 1
    
    ans = 0
    for i in range(9 * 60, 21 * 60 + 1):
        if timestamp[p][i] == 1:
            ans += 1

    print(1260 - 540 - ans)