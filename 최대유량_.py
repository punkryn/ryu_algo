# https://www.acmicpc.net/problem/6086
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

def convert(w):
    if ord(w) <= ord('Z'):
        return ord(w) - ord('A')
    return ord(w) - ord('a') + 26

if __name__ == '__main__':
    n = int(si())
    graph = [[] for _ in range(52)]
    for _ in range(n):
        a, b, w = si().split()
        u = convert(a)
        v = convert(b)
        w = int(w)
        e1 = Edge(v, w)
        e2 = Edge(u, w)
        e1.dual = e2
        e2.dual = e1
        graph[u].append(e1)
        graph[v].append(e2)

    S, E = convert('A'), convert('Z')
    total = 0
    while True:
        prev = [-1] * 52
        path = [None] * 52
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

        flow = float('inf')
        idx = E
        while idx != S:
            flow = min(flow, path[idx].spare())
            idx = prev[idx]
        
        idx = E
        while idx != S:
            path[idx].addFlow(flow)
            idx = prev[idx]
        
        total += flow
    print(total)