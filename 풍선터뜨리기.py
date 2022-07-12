# https://www.acmicpc.net/problem/2346
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    parent[y] = x

if __name__ == '__main__':
    n = int(si())
    b = list(mis())
    parent = [i for i in range(n)]
    idx = 0
    ans = []
    for i in range(n):
        ans.append(idx + 1)
        move = b[idx]
        print(move)
        union((idx - 1) % n, idx)
        while move != 0:
            if move > 0:
                idx = find_parent((idx + 1) % n)
                move -= 1
            else:
                idx = find_parent((idx - 1) % n)
                move += 1
        print(idx, parent)
    print(*ans)