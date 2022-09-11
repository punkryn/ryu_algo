# https://www.acmicpc.net/problem/2668
import sys
sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def dfs(x, start):
    if visited[x]:
        if x == start:
            ans.append(x)
        return
    
    visited[x] = 1
    dfs(table[x], start)

if __name__ == '__main__':
    n = int(si())
    table = [0] + [int(si()) for _ in range(n)]
    
    ans = []
    for i in range(1, n + 1):
        visited = [0] * (n + 1)
        dfs(i, i)
    
    print(len(ans))
    for x in sorted(ans):
        print(x)