# https://www.acmicpc.net/problem/1595
import sys
si = sys.stdin.readline

def DFS(x, prev=0, total=0):
    global ans, root
    if prev != 0 and len(tree[x]) == 1:
        if total > ans:
            ans = total
            root = x
        return
    
    for nxt, cost in tree[x]:
        if nxt == prev: continue
        DFS(nxt, x, total + cost)

if __name__ == '__main__':
    tree = [[] for _ in range(10001)]
    while True:
        try:
            a, b, c = map(int, si().split())
            tree[a].append((b, c))
            tree[b].append((a, c))
        except:
            break
    
    ans = 0
    root = 1
    DFS(root)
    ans = 0
    DFS(root)
    print(ans)