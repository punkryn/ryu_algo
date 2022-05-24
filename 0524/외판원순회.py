# https://www.acmicpc.net/problem/2098
import sys
si = sys.stdin.readline

INF = int(1e9)
def DFS(x, state):
    if state == ans_bits:
        return INF if matrix[x][0] == 0 else matrix[x][0]
    
    if dp[x][state] != -1:
        return dp[x][state]
    
    dp[x][state] = INF
    for i in range(n):
        if matrix[x][i] == 0 or (state & (1 << i) == (1 << i)):
            continue

        dp[x][state] = min(dp[x][state], matrix[x][i] + DFS(i, state | (1 << i)))
    return dp[x][state]            

if __name__ == '__main__':
    n = int(si())
    matrix = [list(map(int, si().split())) for _ in range(n)]
    dp = [[-1 for _ in range(1 << n)] for _ in range(n)]
    
    ans_bits = (1 << n) - 1
    print(DFS(0, 1))