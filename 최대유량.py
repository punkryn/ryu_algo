# https://www.acmicpc.net/problem/6086
import sys
from collections import deque
si = sys.stdin.readline

def convert(w):
    if ord(w) <= ord('Z'):
        return ord(w) - ord('A')
    return ord(w) - ord('a') + 26

if __name__ == '__main__':
    n = int(si())
    graph = [[] for _ in range(52)]
    c = [[0] * 52 for _ in range(52)]
    f = [[0] * 52 for _ in range(52)]
    for _ in range(n):
        a, b, w = si().split()
        u = convert(a)
        v = convert(b)
        w = int(w)
        c[u][v] += w
        c[v][u] += w
        graph[u].append(v)
        graph[v].append(u)

    total = 0
    s, e = convert('A'), convert('Z')

    while True:
        prev = [-1] * 52
        q = deque([s])
        while q and prev[e] == -1:
            cur = q.popleft()

            for nxt in graph[cur]:
                if c[cur][nxt] - f[cur][nxt] > 0 and prev[nxt] == -1:
                    q.append(nxt)
                    prev[nxt] = cur
                    if nxt == e:
                        break
        
        if prev[e] == -1:
            break

        flow = float('inf')
        idx = e
        while idx != s:
            flow = min(flow, c[prev[idx]][idx] - f[prev[idx]][idx])
            idx = prev[idx]
        
        idx = e
        while idx != s:
            f[prev[idx]][idx] += flow
            f[idx][prev[idx]] -= flow
            idx = prev[idx]
        
        total += flow
    print(total)