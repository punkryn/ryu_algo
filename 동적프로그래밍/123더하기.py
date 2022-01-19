# https://acmicpc.net/problem/9095
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    # setlist = {
    #     1: {'1'},
    #     2: {'11', '2'},
    #     3: {'111', '12', '21', '3'}
    # }

    # for i in range(4, n + 1):
    #     setlist[i] = set()
    #     for j in range(1, i):
    #         for v1 in setlist[j]:
    #             for v2 in setlist[i-j]:
    #                 setlist[i].add(v1+v2)
    # print(len(setlist[n]))

    dp = [0, 1, 2, 4] + [0] * (n - 3)
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])

if __name__ == '__main__':
    T = int(si())
    for _ in range(T):
        main()