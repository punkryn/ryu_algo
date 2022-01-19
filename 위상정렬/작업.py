# https://acmicpc.net/problem/2056
import sys
from collections import deque
si = sys.stdin.readline

def main():
    n = int(si())
    indegree = [0] * (n + 1)
    T = [0] * (n + 1)
    T_done = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        work = list(map(int, si().split()))
        T[i] = work[0]
        for num in range(2, 2 + work[1]):
            graph[work[num]].append(i)
            indegree[i] += 1
    
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            T_done[i] = T[i]
    
    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            indegree[nxt] -= 1
            T_done[nxt] = max(T_done[nxt], T_done[cur] + T[nxt])
            if indegree[nxt] == 0:
                q.append(nxt)
    # print(T_done)
    print(max(T_done))

if __name__ == '__main__':
    main()