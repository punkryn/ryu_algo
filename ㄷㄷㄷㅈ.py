# https://www.acmicpc.net/problem/19535
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    tree = []
    edge_cnt = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = map(int, si().split())
        tree.append((u, v))
        edge_cnt[u] += 1
        edge_cnt[v] += 1
    
    du, ga = 0, 0
    for s, e in tree:
        du += (edge_cnt[s] - 1) * (edge_cnt[e] - 1)
    
    for i in range(1, n + 1):
        if edge_cnt[i] >= 3:
            tmp = edge_cnt[i]
            ga += (tmp * (tmp - 1) * (tmp - 2)) // 6
    
    print('D' if du > ga * 3 else 'G' if du < ga * 3 else 'DUDUDUNGA')