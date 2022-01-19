# https://acmicpc.net/problem/14676
import sys
from collections import deque
si = sys.stdin.readline

def main():
    n, m, k = map(int, si().split())
    graph = [[] for _ in range(n + 1)]
    rev = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for _ in range(m):
        x, y = map(int, si().split())
        graph[x].append(y)
        rev[y].append(x)
        indegree[y] += 1
    
    queries = [list(map(int, si().split())) for _ in range(k)]
    degree = [0] * (n + 1)
    cnt = [0] * (n + 1)
    ans = True
    
    for query in queries:
        op, b = query
        if op == 1:
            if degree[b] < indegree[b]:
                ans = False
            cnt[b] += 1
            if cnt[b] == 1:
                for y in graph[b]:
                    degree[y] += 1
        else:
            if cnt[b] == 0:
                ans = False
            cnt[b] -= 1
            if cnt[b] == 0:
                for y in graph[b]:
                    degree[y] -= 1
    
    if not ans:
        print('Lier!')
    else:
        print('King-God-Emperor')

if __name__ == '__main__':
    main()