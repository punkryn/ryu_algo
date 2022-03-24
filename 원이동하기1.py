import sys
import math
si = sys.stdin.readline

def go(cur, prev, depth):
    global rad, node
    if rad < depth:
        rad = depth
        node = cur
    for nxt in tree[cur]:
        if nxt == prev: continue
        go(nxt, cur, depth + 1)
    

if __name__ == '__main__':
    n = int(si())
    circles = [list(map(int, si().split())) for _ in range(n)]
    circles.sort(key=lambda x: x[2])
    circles.append([0, 0, 2000000])
    
    tree = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n + 1):
            if circles[i][2] == circles[j][2]:
                continue

            d = math.sqrt((circles[i][0] - circles[j][0]) ** 2 + (circles[i][1] - circles[j][1]) ** 2)
            if abs(circles[i][2] - circles[j][2]) > d:
                tree[i].append(j)
                tree[j].append(i)
                break
    
    rad = 0
    node = -1
    go(n, -1, 0)
    go(node, -1, 0)
    print(rad)