# https://www.acmicpc.net/problem/1548
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = list(map(int, si().split()))

    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        a.sort()
        ans = 0
        for i in range(n - 2):
            tmp = a[i] + a[i + 1]
            length = 2
            for j in range(i + 2, n):
                if tmp > a[j]:
                    length += 1
            ans = max(ans, length)
        print(ans)