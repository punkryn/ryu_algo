# https://www.acmicpc.net/problem/14427
import sys
si = sys.stdin.readline

def init(s, e, x):
    if s == e:
        min_seg_tree[x] = [a[s], s]
        return [a[s], s]
    
    mid = (s + e) // 2

    min_seg_tree[x] = min(init(s, mid, x * 2), init(mid + 1, e, x * 2 + 1))
    return min_seg_tree[x]
    
def update(s, e, x, left, right, value):
    if left > e or right < s:
        return
    
    if s == e:
        min_seg_tree[x] = [value, s]
        return
    
    mid = (s + e) // 2
    update(s, mid, x * 2, left, right, value)
    update(mid + 1, e, x * 2 + 1, left, right, value)

    idx = x * 2
    if min_seg_tree[x * 2][0] > min_seg_tree[x * 2 + 1][0]:
        idx = x * 2 + 1
    
    min_seg_tree[x] = [min_seg_tree[idx][0], min_seg_tree[idx][1]]


if __name__ == '__main__':
    n = int(si())
    a = [0] + list(map(int, si().split()))
    m = int(si())

    min_seg_tree = [[0, 0] for _ in range(n * 4)]
    init(1 , n, 1)
    for _ in range(m):
        query = list(map(int, si().split()))
        if query[0] == 1:
            update(1, n, 1, query[1], query[1], query[2])
        else:
            print(min_seg_tree[1][1])