# https://acmicpc.net/problem/2637
import sys
from collections import deque
si = sys.stdin.readline

def main():
    n = int(si())
    indegree = [0] * (n + 1)
    m = int(si())
    graph = [[] for _ in range(n + 1)]
    cnt = [0] * (n + 1)
    for _ in range(m):
        x, y, k = map(int, si().split())
        graph[y].append((x, k))
        indegree[x] += 1
    
    q = deque()
    basics = []
    table = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            basics.append(i)
            table[i][i] = 1

    while q:
        cur = q.popleft()    
        # cnt[cur] += cur_cnt
        for nxt, nxt_cnt in graph[cur]:
            for basic in basics:
                table[nxt][basic] += table[cur][basic] * nxt_cnt
            indegree[nxt] -= 1
            cnt[cur] += nxt_cnt
            if indegree[nxt] == 0:
                q.append(nxt)
    # print(table)
    for basic in basics:
        print(basic, table[n][basic])

if __name__ == '__main__':
    main()