# https://www.acmicpc.net/problem/1005
import sys
from collections import deque
si = sys.stdin.readline
def main():
    n, k = map(int, si().split())
    D = list(map(int, si().split()))
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        x, y = map(int, si().split())
        indegree[y] += 1
        graph[x].append(y)
    w = int(si())

    q = deque()
    prev = [0] * (n + 1)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            prev[i] = D[i-1]

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            prev[nxt] = max(prev[cur] + D[nxt-1], prev[nxt])
            if indegree[nxt] == 0:
                q.append(nxt)
    print(prev[w])
                

if __name__ == '__main__':
    T = int(si())
    for _ in range(T):
        main()