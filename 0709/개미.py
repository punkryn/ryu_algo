# https://www.acmicpc.net/problem/14942
import sys
si = sys.stdin.readline

def find_parent(x, prev):
    for nxt, cost in tree[x]:
        if nxt == prev:
            continue
        p[0][nxt] = x
        d[0][nxt] = cost
        find_parent(nxt, x)

if __name__ == '__main__':
    n = int(si())
    ants = [0] + [int(si()) for _ in range(n)]
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = map(int, si().split())
        tree[a].append((b, c))
        tree[b].append((a, c))
    
    p = [[0] * (n + 1) for _ in range(17)]
    d = [[0] * (n + 1) for _ in range(17)]
    p[0][1] = 1
    find_parent(1, 0)
    for i in range(1, 17):
        for j in range(1, n + 1):
            p[i][j] = p[i - 1][p[i - 1][j]]
            d[i][j] = d[i - 1][j] + d[i - 1][p[i - 1][j]]
    
    print(1)
    for i in range(2, n + 1):
        e = ants[i]
        for j in range(16, -1, -1):
            if d[j][i] <= e:
                e -= d[j][i]
                i = p[j][i]
        print(i)