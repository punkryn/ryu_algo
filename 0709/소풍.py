# https://www.acmicpc.net/problem/2026
import sys
si = sys.stdin.readline

def go(x, cur):
    if len(cur) == k:
        for i in sorted(list(cur)):
            print(i)
        exit()

    for i in range(1, n + 1):
        if i in cur or friends[i] < k - 1: continue
        if graph[x][i] and canConnect(cur, i):
            cur.add(i)
            go(i, cur)
            cur.remove(i)
            
def canConnect(cur, i):
    for c in cur:
        if not graph[i][c]:
            return False
    return True

if __name__ == '__main__':
    k, n, f = map(int, si().split())
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    friends = [0] * (n + 1)

    for _ in range(f):
        a, b = map(int, si().split())
        graph[a][b] = True
        graph[b][a] = True
    
        friends[a] += 1
        friends[b] += 1
    
    cur = set()
    for i in range(1, n + 1):
        if friends[i] < k - 1: continue
        cur.add(i)
        go(i, cur)
        cur.remove(i)
    print(-1)