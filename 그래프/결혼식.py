# https://www.acmicpc.net/problem/5567
import sys
from collections import deque
si = sys.stdin.readline

def main():
    n = int(si())
    m = int(si())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, si().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [-1] * (n + 1)
    q = deque()
    q.append(1)
    visited[1] = 0
    ans = 0
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if visited[nxt] != -1:
                 continue
            visited[nxt] = visited[cur] + 1
            q.append(nxt)
    
    for num in visited[1:]:
        if 1 <= num <= 2:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()