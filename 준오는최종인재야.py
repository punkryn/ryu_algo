# https://www.acmicpc.net/problem/14657

import sys
import math
si = sys.stdin.readline


def main():
    n, t = map(int, si().split())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n-1):
        a, b, c = map(int, si().split())
        tree[a].append((c, b))
        tree[b].append((c, a))

    ans = 0
    ans2 = int(1e9)
    def dfs(cur, prev, time):
        nonlocal ans, ans2
        heights = []
        for cost, nxt in tree[cur]:
            if prev == nxt: continue
            tmp, tmp2 = dfs(nxt, cur, time + cost)
            heights.append((tmp, tmp2 + cost))
        if len(heights) == 0:
            return 0, 0
        
        heights.sort()
        if len(heights) >= 2:
            if ans <= heights[len(heights) - 1][0] + heights[len(heights) - 2][0] + 2:
                ans = heights[len(heights) - 1][0] + heights[len(heights) - 2][0] + 2
                ans2 = heights[len(heights) - 1][1] + heights[len(heights) - 2][1]
        
        return heights[-1][0] + 1, heights[-1][1]
    h = dfs(1, -1, 0)
    if h[0] > ans:
        print(math.ceil(h[1] / t))
    elif h[0] < ans:
        print(math.ceil(ans2 / t))

if __name__ == '__main__':
    main()