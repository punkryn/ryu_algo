# https://www.acmicpc.net/problem/14719
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    h, w = map(int, si().split())
    heights = list(map(int, si().split()))
    ans = 0
    
    MAP = [[0] * w for _ in range(h)]
    mh = [0] * w
    m = -1
    for i in range(w - 1, -1, -1):
        if m < heights[i]:
            m = heights[i]
        mh[i] = m

    s = heights[0]
    for i in range(1, w - 1):
        g = min(mh[i], s) - heights[i]
        if g > 0:
            ans += g
        s = max(s, heights[i])
    
    print(ans)