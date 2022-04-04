# https://www.acmicpc.net/problem/12978
import sys
sys.setrecursionlimit(int(1e6))
si = sys.stdin.readline

INF = int(1e6)

def DFS(x, prev, flag):
    if dp[x][flag] != INF:
        return dp[x][flag]
    ret = 0 if flag else 1
    for nxt in tree[x]:
        if nxt == prev: continue
        if flag:
            ret += DFS(nxt, x, 0)
        else:
            ret += min(DFS(nxt, x, 0), DFS(nxt, x, 1))
    dp[x][flag] = ret
    print(dp)
    return ret

if __name__ == '__main__':
    n = int(si())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, si().split())
        tree[a].append(b)
        tree[b].append(a)
    
    dp = [[INF, INF] for _ in range(n + 1)]
    dp[0][0], dp[0][1] = 0, 0
    print(min(DFS(1, 0, 0), DFS(1, 0, 1)))