# https://www.acmicpc.net/problem/1167
import sys
sys.setrecursionlimit(int(1e6))
si = sys.stdin.readline

def DFS(x, prev, total):
    global r, v
    if r < total:
        r = total
        v = x
    for nxt, cost in tree[x]:
        if nxt == prev: continue
        DFS(nxt, x, total + cost)

if __name__ == '__main__':
    v = int(si())
    tree = [[] for _ in range(v + 1)]
    for _ in range(v):
        info = list(map(int, si().split()))
        for i in range(1, len(info) - 1, 2):
            tree[info[0]].append((info[i], info[i + 1]))
    
    r = 0
    v = 0
    DFS(1, 0, 0)
    DFS(v, 0, 0)
    print(r)