# https://www.acmicpc.net/problem/21757
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = list(map(int, si().split()))
    ps = [0] * n
    ps[0] = a[0]
    for i in range(1, n):
        ps[i] = ps[i - 1] + a[i]
    s = ps[n - 1] // 4    
    if ps[n - 1] % 4 != 0:
        print(0)
        exit()
    
    cnt = [0] * 4
    cnt[0] = 1
    for i in range(n - 1):
        if ps[i] == 3 * s:
            cnt[3] += cnt[2]
        if ps[i] == 2 * s:
            cnt[2] += cnt[1]
        if ps[i] == s:
            cnt[1] += cnt[0]
    print(cnt[3])