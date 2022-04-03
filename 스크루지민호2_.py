# https://www.acmicpc.net/problem/12978
import sys
si = sys.stdin.readline
sys.setrecursionlimit(1000010)

INF = int(1e6)

def go(x, prev, flag):
    if dp[x][flag] != INF:
        return dp[x][flag]
    
    ret = 0 if flag else 1
    for nxt in tree[x]:
        if nxt == prev: continue
        if flag:
            ret += go(nxt, x, 0)
        else:
            ret += min(go(nxt, x, 0), go(nxt, x, 1))
    dp[x][flag] = ret
    return ret


if __name__ == '__main__':
    n = int(si())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, si().split())
        tree[a].append(b)
        tree[b].append(a)
    
    dp = [[INF, INF] for _ in range(n + 1)]
    dp[0][0] = 0
    dp[0][1] = 0
    print(min(go(1, 0, 0), go(1, 0, 1)))