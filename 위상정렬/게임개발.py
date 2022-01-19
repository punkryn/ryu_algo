# https://acmicpc.net/problem/1516
import sys
from collections import deque
si = sys.stdin.readline

def main():
    n = int(si())
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    time = [0] * (n + 1)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        order = list(map(int, si().split()))
        time[i] = order[0]
        for pre in order[1:-1]:
            indegree[i] += 1
            graph[pre].append(i)

    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]
    
    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            indegree[nxt] -= 1
            dp[nxt] = max(dp[nxt], dp[cur] + time[nxt])
            if indegree[nxt] == 0:
                q.append(nxt)
    
    for v in dp[1:]:
        print(v)

if __name__ == '__main__':
    main()