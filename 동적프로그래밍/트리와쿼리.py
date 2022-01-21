# https://acmicpc.net/problem/15681
import sys
sys.setrecursionlimit(100100)
si = sys.stdin.readline

def main():
    n, r, q = map(int, si().split())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n -1):
        u, v = map(int, si().split())
        tree[u].append(v)
        tree[v].append(u)

    dp = [0] * (n + 1)
    def dfs(x, par):
        cnt = 1
        for nxt in tree[x]:
            if nxt == par:
                continue    
            cnt += dfs(nxt, x)
        dp[x] = cnt
        return cnt

    dfs(r, -1)    
    for _ in range(q):
        query = int(si())
        print(dp[query])

if __name__ == '__main__':
    main()