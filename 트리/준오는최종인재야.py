# https://www.acmicpc.net/problem/14657

import sys
import math
si = sys.stdin.readline
sys.setrecursionlimit(100000)

def main():
    n, t = map(int, si().split())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n-1):
        a, b, c = map(int, si().split())
        tree[a].append((c, b))
        tree[b].append((c, a))

    minCost = 0
    farthest = 0
    diameter = 0
    def dfs(cur, prev, depth, cost):
        nonlocal farthest, diameter, minCost
        if diameter < depth:
            diameter = depth
            farthest = cur
            minCost = cost
        elif diameter == depth and minCost > cost:
            minCost = cost
            farthest = cur
        
        for cst, nxt in tree[cur]:
            if nxt == prev: continue
            dfs(nxt, cur, depth + 1, cost + cst)
    
    dfs(1, -1, 0, 0)

    minCost = 0
    diameter = 0
    dfs(farthest, -1, 0, 0)

    print(math.ceil(minCost / t))