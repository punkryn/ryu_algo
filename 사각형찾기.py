# https://www.acmicpc.net/problem/12024
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    a = [list(map(int, si().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(n):
                if i == j or j == k or i == k: continue
                if a[i][k] and a[k][j]:
                    cnt += 1
            ans += cnt * (cnt - 1)
    print(ans)