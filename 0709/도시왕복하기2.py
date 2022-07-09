# https://www.acmicpc.net/problem/2316
import sys
from collections import deque
si = sys.stdin.readline

class Edge:
    def __init__(self, to, c):
        self.to = to
        self.c = c
        self.f = 0
        self.dual = None
    
    def spare(self):
        return self.c - self.f
    
    def addFlow(self, flow):
        self.f += flow
        self.dual.f -= flow

if __name__ == '__main__':
    n, p = map(int, si().split())
    
    graph = [[] for _ in range((n + 1) * 2)]
    for i in range(2, (n + 1) * 2, 2):
        e1 = Edge(i + 1, 1)
        e2 = Edge(i, 0)
        e1.dual = e2
        e2.dual = e1
        graph[i].append(e1)
        graph[i + 1].append(e2)
    for _ in range(p):
        u, v = map(int, si().split())
        e1 = Edge(u * 2, float('inf'))
        re1 = Edge(u * 2 + 1, 0)
        e2 = Edge(v * 2, float('inf'))
        re2 = Edge(v * 2 + 1, 0)
        e1.dual = re1
        re1.dual = e1
        e2.dual = re2
        re2.dual = e2
        graph[u * 2 + 1].append(e1)
        graph[v * 2 + 1].append(e2)
        graph[u * 2].append(re1)
        graph[v * 2].append(re2)
    
    S, E = 3, 4
    total = 0
    while True:
        prev = [-1] * ((n + 1) * 2)
        path = [None] * ((n + 1) * 2)
        q = deque([S])
        while q and prev[E] == -1:
            cur = q.popleft()

            for e in graph[cur]:
                nxt = e.to
                if prev[nxt] == -1 and e.spare() > 0:
                    prev[nxt] = cur
                    path[nxt] = e
                    q.append(nxt)
                    if nxt == E:
                        break
        if prev[E] == -1:
            break

        idx = E
        flow = float('inf')
        while idx != S:
            flow = min(flow, path[idx].spare())
            idx = prev[idx]

        idx = E
        while idx != S:
            path[idx].addFlow(flow)
            idx = prev[idx]
        total += flow
    print(total)