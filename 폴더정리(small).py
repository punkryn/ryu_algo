# https://www.acmicpc.net/problem/22860
import sys
si = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def go(x):
    if x in children:
        for file in children[x]:
            if file not in ans:
                ans[file] = 0
            ans[file] += 1

    if x in tree:
        for nxt in tree[x]:
            go(nxt)

if __name__ == '__main__':
    n, m = map(int, si().split())
    tree = dict()
    children = dict()
    for _ in range(n + m):
        p, f, c = si().split()
        if c == '1':
            if p not in tree:
                tree[p] = []
            tree[p].append(f)
        else:
            if p not in children:
                children[p] = []
            children[p].append(f)

    # folder check, file check
    for _ in range(int(si())):
        query = si().strip()
        ans = dict()
        q = query.split('/')[-1]
        go(q)
        print(len(ans), sum(ans.values()))