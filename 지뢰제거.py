# https://www.acmicpc.net/problem/9077
import sys
si = sys.stdin.readline

def init(seg_tree, coordinate, s, e, x):
    if s == e:
        seg_tree[x] = [coordinate[s][1], coordinate[s][1]]
        return seg_tree[x]
    
    mid = (s + e) // 2
    tmp1 = init(seg_tree, coordinate, s, mid, x * 2)
    tmp2 = init(seg_tree, coordinate, mid + 1, e, x * 2 + 1)
    maxv = max(*tmp1, *tmp2)
    minv = min(*tmp1, *tmp2)
    seg_tree[x] = [maxv, minv]
    return seg_tree[x]

def find_minmax(seg_tree, coordinate, s, e, x, left, right):
    if right < s or e < left:
        return [-1, int(1e6)]
    
    if left <= s and e <= right:
        return seg_tree[x]
    
    mid = (s + e) // 2
    tmp1 = find_minmax(seg_tree, coordinate, s, mid, x * 2, left, right)
    tmp2 = find_minmax(seg_tree, coordinate, mid + 1, e, x * 2 + 1, left, right)
    
    maxv = 0
    minv = int(1e6)
    for t in tmp1 + tmp2:
        if t == int(1e6) or t == -1: continue
        if t > maxv:
            maxv = t
        if t < minv:
            minv = t
    return [maxv, minv]

def main():
    n = int(si())
    coordinate = sorted([list(map(int, si().split())) for _ in range(n)])
    seg_tree = [[0, 0] for _ in range(n * 4)] # max min
    init(seg_tree, coordinate, 0, n - 1, 1)
    # print(find_minmax(seg_tree, coordinate, 0, n - 1, 1, 0, 0))

    r = -1
    ans = 0
    width = 0
    cnt = 0
    for l in range(n):
        while r + 1 < n and width <= 10:
            r += 1
            width = (coordinate[r][0] - coordinate[l][0])
            if width <= 10:
                maxv, minv = find_minmax(seg_tree, coordinate, 0, n - 1, 1, l, r)
                if maxv - minv <= 10:
                    cnt += 1
                else:
                    break
        ans = max(ans, cnt)
        cnt -= 1
        if l + 1 < n:
            width -= (coordinate[l + 1][0] - coordinate[l][0])
            if width <= 10:
                maxv, minv = find_minmax(seg_tree, coordinate, 0, n - 1, 1, l + 1, r)
                if maxv - minv <= 10:
                    cnt += 1
                    ans = max(ans, cnt)

    print(ans)

if __name__ == '__main__':
    for _ in range(int(si())):
        main()