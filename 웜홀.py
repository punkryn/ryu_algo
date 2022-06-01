# https://www.acmicpc.net/problem/1865
import sys
si = sys.stdin.readline
INF = int(1e9)
def bf(x, n, edges):
    distance = [INF] * (n + 1)
    distance[x] = 0
    for i in range(n):
        for j in range(len(edges)):
            cur = edges[j][0]
            nxt_node = edges[j][1]
            cost = edges[j][2]

            if distance[nxt_node] > distance[cur] + cost:
                distance[nxt_node] = distance[cur] + cost
                if i == n - 1:
                    return True
    
    return False

def main():
    n, m, w = map(int, si().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, si().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    
    for _ in range(w):
        s, e, t = map(int, si().split())
        edges.append((s, e, -t))
    
    if bf(1, n, edges):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    for _ in range(int(si())):
        main()