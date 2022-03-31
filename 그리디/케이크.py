# https://www.acmicpc.net/problem/1088
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    w = list(map(int, si().split()))
    m = int(si())

    a = [(x, 0) for x in w]
    
    ans = max(a)[0] - min(a)[0]
    for _ in range(m):
        size = a[0][0]
        idx = 0
        for i in range(1, n):
            if a[i][0] > size:
                size = a[i][0]
                idx = i

        original = size * (a[idx][1] + 1)
        cut = original / (a[idx][1] + 2)
        a[idx] = (cut, a[idx][1] + 1)
        ans = min(ans, max(a)[0] - min(a)[0])
print('{:.20f}'.format(ans))