# https://www.acmicpc.net/problem/11509
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    h = list(map(int, si().split()))
    flags = [0] * 1000001
    ans = 0
    for i in range(n):
        if flags[h[i]] == 0:
            ans += 1
            flags[h[i] - 1] += 1
        else:
            flags[h[i]] -= 1
            flags[h[i] - 1] += 1
    print(ans)