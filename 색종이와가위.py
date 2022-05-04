# https://www.acmicpc.net/problem/20444
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, si().split())
    l, r = 0, n // 2 + 1
    while l <= r:
        mid = (l + r) // 2
        cnt = (mid + 1) * (n - mid + 1)
        if cnt < k:
            l = mid + 1
        elif cnt > k:
            r = mid - 1
        else:
            print('YES')
            exit()
    print('NO')