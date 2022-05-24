# https://www.acmicpc.net/problem/1766
import sys
import heapq
si = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, si().split())
        graph[a].append(b)
        indegree[b] += 1
    
    q = []
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(q, i)
            visited[i] = 1
    ans = []
    while q:
        cur = heapq.heappop(q)
        ans.append(cur)
        
        for nxt in graph[cur]:
            if visited[nxt]: continue
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                visited[nxt] = 1
                heapq.heappush(q, nxt)
    for i in range(1, n + 1):
        if visited[i] == 0:
            ans.append(i)
    print(*ans)