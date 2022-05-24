# https://www.acmicpc.net/problem/2342
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
si = stdin.readline

def move(s, e):
    if s == 0: return 2
    elif s == e: return 1
    elif abs(s - e) % 2 == 0: return 4
    else: return 3

def go(depth, l, r):
    if depth >= len(order) - 1:
        return 0
    
    if dp[depth][l][r] != 0:
        print(dp)
        return dp[depth][l][r]
    
    dp[depth][l][r] = min(move(l, order[depth]) + go(depth + 1, order[depth], r), move(r, order[depth]) + go(depth + 1, l, order[depth]))
    return dp[depth][l][r]

if __name__ == '__main__':
    order = list(map(int, si().split()))
    n = len(order)
    dp = [[[0] * 5 for _ in range(5)] for _ in range(n)]
    print(go(0, 0, 0))