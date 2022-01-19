# https://acmicpc.net/problem/9470
import sys
from collections import deque
si = sys.stdin.readline

def main():
    k, m, p = map(int, si().split())
    graph = [[] for _ in range(m + 1)]
    indegree = [0] * (m + 1)
    orders = [1] * (m + 1)
    number = [0] * (m + 1)
    for _ in range(p):
        a, b = map(int, si().split())
        graph[a].append(b)
        indegree[b] += 1

    q = deque()
    for i in range(1, m + 1):
        if indegree[i] == 0:
            q.append(i)
        
    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if orders[nxt] == orders[cur]:
                number[nxt] += 1
            elif orders[nxt] < orders[cur]:
                orders[nxt] = max(orders[cur], orders[nxt])
                number[nxt] = 1

            if indegree[nxt] == 0:
                q.append(nxt)
                if number[nxt] >= 2:
                    orders[nxt] += 1

    print(k, orders[m])

if __name__ == '__main__':
    T = int(si())
    for _ in range(T):
        main()