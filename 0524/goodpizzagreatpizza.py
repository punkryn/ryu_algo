# https://www.acmicpc.net/problem/17235
# https://greimul.tistory.com/33?category=813720
import sys
import math
si = sys.stdin.readline

INF = int(1e10)

def get_dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

if __name__ == '__main__':
    n = int(si())
    maxh, minh, maxw, minw = -INF, INF, -INF, INF
    for _ in range(n):
        x, y = map(int, si().split())
        maxh = max(maxh, x + y)
        minh = min(minh, x + y)
        maxw = max(maxw, y - x)
        minw = min(minw, y - x)

    p1 = ((minh - maxw) / 2, (minh - maxw) / 2 + maxw)
    p2 = ((maxh - minw) / 2, (maxh - minw) / 2 + minw)
    p3 = ((maxh - maxw) / 2, (maxh - maxw) / 2 + maxw)
    p4 = ((minh - minw) / 2, (minh - minw) / 2 + minw)
    r = max(get_dist(p1, p3), get_dist(p2, p3), get_dist(p2, p4), get_dist(p4, p1))
    ans = r
    if ans.is_integer():
        print(int(ans))
    else:
        print(f'{ans:.1f}')