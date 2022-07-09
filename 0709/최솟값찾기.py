# https://www.acmicpc.net/problem/11003
import sys
si = sys.stdin.readline

INF = int(1e10)
def init(s, e, v):
    if s == e:
        tree[v] = a[s]
        return a[s]
    
    mid = (s + e) // 2
    tree[v] = min(init(s, mid, v * 2), init(mid + 1, e, v * 2 + 1))
    return tree[v]

def query(s, e, v, l, r):
    if e < l or r < s:
        return INF
    
    if l <= s and e <= r:
        return tree[v]
    
    mid = (s + e) // 2
    return min(query(s, mid, v * 2, l, r), query(mid + 1, e, v * 2 + 1, l, r))

if __name__ == '__main__':
    n, l = map(int, si().split())
    a = list(map(int, si().split()))
    tree = [0] * (n * 4)
    init(0, n - 1, 1)
    for i in range(n):
        print(query(0, n - 1, 1, max(0, i - l + 1), i), end=' ')