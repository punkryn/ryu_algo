# https://www.acmicpc.net/problem/2098
import sys
si = sys.stdin.readline

def tsp(x, state):
    if state == base:
        return matrix[x][0] if matrix[x][0] != 0 else INF
    
    if dp[x][state] != -1:
        return dp[x][state]
    
    dp[x][state] = INF
    for i in range(n):
        if matrix[x][i] == 0 or state & (1 << i): continue
        dp[x][state] = min(dp[x][state], tsp(i, state | (1 << i)) + matrix[x][i])
    return dp[x][state]

if __name__ == '__main__':
    n = int(si())
    matrix = [list(map(int, si().split())) for _ in range(n)]
    INF = float('inf')
    dp = [[-1] * (1 << n) for _ in range(n)]
    base = (1 << n) - 1

    print(tsp(0, 1))