# https://www.acmicpc.net/problem/1389
import sys
from collections import deque
si = sys.stdin.readline

def main():
    n, m = map(int, si().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, si().split())
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(i):
        visited = [-1] * (n + 1)
        q = deque()
        q.append(i)
        visited[i] = 0
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                if visited[nxt] != -1: continue
                visited[nxt] = visited[cur] + 1
                q.append(nxt)
        return sum(visited[1:])            
    
    ans = int(1e9)
    res = 0
    for i in range(1, n + 1):
        tmp = bfs(i)
        if ans > tmp:
            ans = tmp
            res = i
    print(res)

if __name__ == '__main__':
    main()