# https://www.acmicpc.net/problem/2623
import sys
from collections import deque
si = sys.stdin.readline

def main():
    n, m = map(int, si().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    orders = []
    for _ in range(m):
        tmp = list(map(int, si().split()))
        orders.append(tmp)
        for i in range(1, tmp[0]):
            indegree[tmp[i + 1]] += 1
            graph[tmp[i]].append(tmp[i + 1])
    
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    ans = []
    while q:
        cur = q.popleft()
        
        ans.append(cur)

        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    if len(ans) != n:
        print(0)
    else:
        for a in ans:
            print(a)

if __name__ == '__main__':
    main()