# https://www.acmicpc.net/problem/17412
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
    graph = [[] for _ in range(n + 1)]
    for _ in range(p):
        a, b = map(int, si().split())
        e1 = Edge(b, 1)
        e2 = Edge(a, 0)
        e1.dual = e2
        e2.dual = e1
        graph[a].append(e1)
        graph[b].append(e2)
    
    S, E = 1, 2
    total = 0
    while True:
        prev = [-1] * (n + 1)
        path = [None] * (n + 1)
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