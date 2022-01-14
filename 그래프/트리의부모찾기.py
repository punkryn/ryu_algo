# https://www.acmicpc.net/problem/11725
import sys
sys.setrecursionlimit(1000000)
si = sys.stdin.readline

def main():
    n = int(si())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n-1):
        a, b = map(int, si().split())
        graph[a].append(b)
        graph[b].append(a)
    
    nodes = [0] * (n + 1)

    visited = [0] * (n + 1)
    def dfs(x):
        visited[x] = 1
        for nxt in graph[x]:
            if visited[nxt] != 0: continue
            nodes[nxt] = x
            dfs(nxt)
    
    dfs(1)
    for i in range(2, n + 1):
        print(nodes[i])

if __name__ == '__main__':
    main()