# https://www.acmicpc.net/problem/2058
from sys import stdin
si = stdin.readline

def dfs(cur):
    visited[cur] = True
    dp[cur][1] = cur
    for d in e:
        for nxt in [cur + d, cur - d]:
            if nxt in visited and not visited[nxt]:
                dfs(nxt)
                dp[cur][0] += max(dp[nxt][1], dp[nxt][0])
                dp[cur][1] += dp[nxt][0]

if __name__ == '__main__':
    n, m = map(int, si().split())
    state = [int(si()) for _ in range(n)]
    e = [int(si()) for _ in range(m)]
    
    dp = {key: [0, 0] for key in state}
    visited = {key: False for key in state}
    dfs(state[0])
    print(max(dp[state[0]]))