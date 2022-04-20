# https://www.acmicpc.net/problem/2250
import sys
si = sys.stdin.readline

def traverse(x, level):
    global cnt
    if x == -1:
        return 0
    
    if level not in ans:
        ans[level] = [int(1e6), 0]
    if tree[x][0] == -1 and tree[x][1] == -1:
        cnt += 1
        ans[level][0] = min(ans[level][0], cnt)
        ans[level][1] = max(ans[level][1], cnt)
        return 1

    ret = 0
    ret += traverse(tree[x][0], level + 1)
    cnt += 1
    ans[level][0] = min(ans[level][0], cnt)
    ans[level][1] = max(ans[level][1], cnt)
    ret += traverse(tree[x][1], level + 1)
    return ret

if __name__ == '__main__':
    n = int(si())
    tree = [[] for _ in range(n + 1)]
    parent = [0] * (n + 1)
    for _ in range(n):
        a, l, r = map(int, si().split())
        tree[a].append(l)
        tree[a].append(r)
        if l != -1:
            parent[l] = a
        if r != -1:
            parent[r] = a
    
    root = 0
    for i in range(1, n + 1):
        if parent[i] == 0:
            root = i
    cnt = 0
    ans = dict()
    traverse(root, 1)
    
    level, width = 0, 0
    for key in ans:
        w = ans[key][1] - ans[key][0] + 1
        if w > width:
            level = key
            width = w
    print(level, width)