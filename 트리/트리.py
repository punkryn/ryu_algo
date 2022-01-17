# https://www.acmicpc.net/problem/1068
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    parents = list(map(int, si().split()))
    rm = int(si())

    graph = [[] for _ in range(n)]
    root = 0
    leaf = [0] * n
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            if i == rm: continue
            graph[parents[i]].append(i)
    
    def dfs(x):
        if not graph[x]:
            leaf[x] = 1
        
        for nxt in graph[x]:
            dfs(nxt)
            leaf[x] += leaf[nxt]
    
    if rm != root:
        dfs(root)
    print(leaf[root])

if __name__ == '__main__':
    main()