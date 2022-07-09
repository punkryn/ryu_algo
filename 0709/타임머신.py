# https://www.acmicpc.net/problem/11657
import sys
si = sys.stdin.readline
INF = int(1e9)

def bf():
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            nxt = edges[j][1]
            cost = edges[j][2]
            nxt_cost = distance[cur] + cost
            if distance[cur] != INF and distance[nxt] > nxt_cost:
                distance[nxt] = nxt_cost
                if i == n - 1:
                    return True
    return False

if __name__ == '__main__':
    n, m = map(int, si().split())
    edges = [list(map(int, si().split())) for _ in range(m)]
    
    distance = [INF] * (n + 1)
    distance[1] = 0
    if bf():
        print(-1)
    else:
        for i in range(2, n + 1):
            if distance[i] == INF:
                print(-1)
            else:
                print(distance[i])