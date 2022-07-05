# https://www.acmicpc.net/problem/2188
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
    n, m = map(int, si().split())
    graph = [[] for _ in range(n + m + 2)]
    for i in range(1, n + 1):
        e1 = Edge(i, 1)
        e2 = Edge(0, 0)
        e1.dual = e2
        e2.dual = e1
        graph[0].append(e1)
        graph[i].append(e2)
    for i in range(1, n + 1):
        _, *info = map(int, si().split())
        for j in info:
            e1 = Edge(j + n, 1)
            e2 = Edge(i, 0)
            e1.dual = e2
            e2.dual = e1
            graph[i].append(e1)
            graph[j + n].append(e2)
    
    for i in range(n + 1, n + m + 1):
        e1 = Edge(n + m + 1, 1)
        e2 = Edge(i, 0)
        e1.dual = e2
        e2.dual = e1
        graph[i].append(e1)
        graph[n + m + 1].append(e2)
    
    S = 0
    E = n + m + 1
    total = 0
    while True:
        prev = [-1] * (n + m + 2)
        path = [None] * (n + m + 2)
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
        while idx != S:
            path[idx].addFlow(1)
            idx = prev[idx]
        
        total += 1
    print(total)