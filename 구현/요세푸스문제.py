# https://www.acmicpc.net/problem/1158
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, si().split())
    a = [i for i in range(1, n + 1)]
    start = k - 1
    ans = []
    while a:
        if start >= len(a):
            start = start % len(a)
        ans.append(str(a.pop(start)))
        start += k - 1
    print(f'<{", ".join(ans)}>')