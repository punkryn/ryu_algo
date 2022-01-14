# https://www.acmicpc.net/problem/11724
import sys
sys.setrecursionlimit(100000)
si = sys.stdin.readline
def main():
    n, m = map(int, si().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, si().split())
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [0] * 1001
    
    def dfs(x):
        visited[x] = 1
        for nxt in graph[x]:
            if visited[nxt] != 0: continue
            dfs(nxt)
    
    ans = 0
    for i in range(1, n + 1):
        if visited[i] != 0: continue
        dfs(i)
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()