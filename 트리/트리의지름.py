# https://www.acmicpc.net/problem/1967
import sys
sys.setrecursionlimit(100000)
si = sys.stdin.readline

def main():
    n = int(si())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = map(int, si().split())
        tree[a].append((b, c))
        tree[b].append((a, c))

    maxCost = 0
    farthest = 0
    def dfs(cur, prev, cost):
        nonlocal maxCost, farthest
        if maxCost < cost:
            maxCost = cost
            farthest = cur
            
        for nxt, cst in tree[cur]:
            if nxt == prev:
                continue

            dfs(nxt, cur, cost + cst)
    
    dfs(1, -1, 0)
    dfs(farthest, -1, 0)
    print(maxCost)

if __name__ == '__main__':
    main()

# import sys
# si = sys.stdin.readline

# def main():
#     n = int(si())
#     tree = [[] for _ in range(n + 1)]
#     for _ in range(n - 1):
#         a, b, c = map(int, si().split())
#         tree[a].append((b, c))
    
#     ans = [(0, 0)] * (n + 1)
#     for i in range(n, 0, -1):
#         x1, x2 = 0, 0
#         for nxt, cost in tree[i]:
#             t = cost + ans[nxt][0]
#             if t > x1:
#                 x2 = x1
#                 x1 = t
#             elif t > x2:
#                 x2 = t
#         ans[i] = (x1, x2)
#     ans.sort(reverse=True, key=lambda x: sum(x))
#     print(sum(ans[0]))

# if __name__ == '__main__':
#     main()