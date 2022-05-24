# https://www.acmicpc.net/problem/9466
from sys import setrecursionlimit, stdin
setrecursionlimit(int(1e9))
si = stdin.readline

def dfs(x, visited, finished, graph):
    global order, cycle
    visited[x] = order
    order += 1

    for nxt in graph[x]:
        if visited[nxt] == -1:
            dfs(nxt, visited, finished, graph)
        elif not finished[nxt]:
            cycle += visited[x] - visited[nxt] + 1
    finished[x] = True

def main():
    global cycle
    n = int(si())
    s = list(map(int, si().split()))
    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i].append(s[i - 1])
    
    visited = [-1] * (n + 1)
    finished = [False] * (n + 1)
    for i in range(1, n + 1):
        dfs(i, visited, finished, graph)
    print(n - cycle)

if __name__ == '__main__':
    for _ in range(int(si())):
        order, cycle = 0, 0
        main()