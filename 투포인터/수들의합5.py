# https://www.acmicpc.net/problem/2018
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    total = 0
    r = 0
    ans = 0
    for l in range(1, n + 1):
        while r + 1 <= n and total <= n:
            total += r + 1
            r += 1
            if total == n:
                ans += 1
        total -= l
        if total == n:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()