# https://www.acmicpc.net/problem/2042
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def init(left, right, idx):
    if left == right:
        seg[idx] = arr[left]
        return seg[idx]
    
    mid = (left + right) // 2
    ret = init(left, mid, idx * 2) + init(mid + 1, right, idx * 2 + 1)
    seg[idx] = ret
    return ret

def update(left, right, idx, upd_idx, d):
    if right < upd_idx or upd_idx < left:
        return
    
    if left <= upd_idx and upd_idx <= right:
        seg[idx] -= d
    
    if left == right:
        return
    
    mid = (left + right) // 2
    update(left, mid, idx * 2, upd_idx, d)
    update(mid + 1, right, idx * 2 + 1, upd_idx, d)
    
def query(left, right, idx, l, r):
    if right < l or r < left:
        return 0
    
    if l <= left and right <= r:
        return seg[idx]
    
    mid = (left + right) // 2
    return query(left, mid, idx * 2, l, r) + query(mid + 1, right, idx * 2 + 1, l, r)

if __name__ == '__main__':
    n, m, k = mis()
    arr = [int(si()) for _ in range(n)]
    seg = [0] * (n * 4)
    init(0, n - 1, 1)
    for _ in range(k + m):
        a, b, c = mis()
        if a == 1:
            update(0, n - 1, 1, b - 1, arr[b - 1] - c)
            arr[b - 1] = c
        else:
            print(query(0, n - 1, 1, b - 1, c - 1))