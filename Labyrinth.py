# https://www.acmicpc.net/problem/3482
import sys
sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, prev, rad):
    global ans, root
    if len(graph[x]) == 1:
        if ans < rad:
            ans = rad
            root = x

    for nxt in graph[x]:
        if prev == nxt: continue
        DFS(nxt, x, rad + 1)

if __name__ == '__main__':
    for _ in range(int(si())):
        c, r = mis()
        MAP = [si().strip() for _ in range(r)]
        
        graph = [[] for _ in range(r * c)]
        for i in range(1, r - 1):
            for j in range(1, c - 1):
                idx = i * c + j
                if MAP[i][j] == '.':
                    for k in range(4):
                        ni = i + dx[k]
                        nj = j + dy[k]
                        if MAP[ni][nj] == '.':
                            idx_ = ni * c + nj
                            graph[idx_].append(idx)
        root = 0
        for g in graph:
            if g:
                root = g[0]
                break

        if root:
            ans = 0
            DFS(root, -1, 0)
            DFS(root, -1, 0)
            print(f'Maximum rope length is {ans}.')
        else:
            print(f'Maximum rope length is {0}.')