# https://www.acmicpc.net/problem/4803
import sys
from collections import deque
si = sys.stdin.readline

def main():
    case = 0
    while True:
        case += 1
        n, m = map(int, si().split())
        if n == 0 and m == 0: return
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b = map(int, si().split())
            graph[a].append(b)
            graph[b].append(a)
        
        v_cnt, e_cnt = 0, 0
        visited = [0] * (n + 1)
        def dfs(x):
            nonlocal v_cnt, e_cnt
            visited[x] = 1
            v_cnt += 1
            e_cnt += len(graph[x])
            for nxt in graph[x]:
                if visited[nxt] != 0: continue
                dfs(nxt)

        T = 0
        for i in range(1, n + 1):
            v_cnt, e_cnt = 0, 0
            if visited[i] != 0: continue
            dfs(i)
            if e_cnt == (v_cnt - 1) * 2:
                T += 1
        
        if T == 0:
            print(f'Case {case}: No trees.')
        elif T == 1:
            print(f'Case {case}: There is one tree.')
        else:
            print(f'Case {case}: A forest of {T} trees.')

if __name__ == '__main__':
    main()