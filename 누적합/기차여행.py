# https://www.acmicpc.net/problem/10713

import sys
si = sys.stdin.readline

def main():
    n, m = map(int, si().split())
    P = list(map(int, si().split()))
    prices = [0] + [list(map(int, si().split())) for _ in range(n - 1)]

    sequence = [0] * (n + 1)
    for i in range(len(P) - 1):
        start, end = P[i], P[i + 1]
        if start > end:
            start, end = end , start
        sequence[start] += 1
        sequence[end] -= 1
    
    for i in range(1, len(sequence)):
        sequence[i] += sequence[i - 1]

    ans = 0
    for i in range(1, len(sequence) - 1):
        ans += min(sequence[i] * prices[i][0], sequence[i] * prices[i][1] + prices[i][2])
    print(ans)

if __name__ == '__main__':
    main()