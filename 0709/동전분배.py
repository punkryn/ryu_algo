# https://www.acmicpc.net/problem/1943
from sys import stdin
si = stdin.readline

def main():
    n = int(si())
    coin = [list(map(int, si().split())) for _ in range(n)]
    target = sum([v * c for v, c in coin])
    if target % 2 != 0:
        print(0)
        return
    target //= 2
    dp = [0] * (target + 1)
    dp[0] = 1
    for v, c in coin:
        for i in range(target, v - 1, -1):
            if dp[i - v]:
                for j in range(c):
                    if i + v * j <= target:
                        dp[i + v * j] = 1
                        if i + v * j == target:
                            print(1)
                            return
    print(dp[target])

if __name__ == "__main__":
    for _ in range(3):
        main()