# https://www.acmicpc.net/problem/1240
import sys
from collections import deque
si = sys.stdin.readline

def main():
    n, m = map(int, si().split())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, d = map(int, si().split())
        tree[a].append([b, d])
        tree[b].append([a, d])

    queries = [list(map(int, si().split())) for _ in range(m)]

    def dfs(x, prev, target, dist):
        if x == target:
            print(dist)
            return

        for nxt in tree[x]:
            node, d = nxt
            if node == prev:
                continue
            dfs(node, x, target, dist + d)

    def bfs(query, target):
        q = deque()
        q.append(query)
        visited = [-1] * (n + 1)
        visited[query] = 0

        while q:
            cur = q.popleft()
            if cur == target:
                break

            for nxt in tree[cur]:
                nxt_node, dist = nxt
                if visited[nxt_node] != -1: continue
                visited[nxt_node] = visited[cur] + dist
                q.append(nxt_node)
        return visited[target]

    for query in queries:
        # print(bfs(query[0], query[1]))
        dfs(query[0], -1, query[1], 0)
if __name__ == '__main__':
    main()
