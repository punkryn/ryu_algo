# https://www.acmicpc.net/problem/2252
import sys
from collections import deque
si = sys.stdin.readline
def main():
    n, m = map(int, si().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, si().split())
        graph[a].append(b)
        indegree[b] += 1
    
    q = deque()
    # visited = [0] * (n + 1)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            # visited[i] = 1
    ans = []
    while q:
        cur = q.popleft()
        ans.append(cur)
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    print(*ans)

if __name__ == '__main__':
    main()