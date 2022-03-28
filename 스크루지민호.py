# https://www.acmicpc.net/problem/12896
import sys
import math
si = sys.stdin.readline
sys.setrecursionlimit(200000)

def traverse(prev, s, depth):
    global rad, node

    if rad < depth:
        rad = depth
        node = s

    for nxt in tree[s]:
        if prev == nxt: continue
        traverse(s, nxt, depth + 1)

if __name__ == '__main__':
    n = int(si())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x, y = map(int, si().split())
        tree[x].append(y)
        tree[y].append(x)
    
    rad = 0
    node = 0
    traverse(0, 1, 0)
    traverse(0, node, 0)
    print(math.ceil(rad / 2))