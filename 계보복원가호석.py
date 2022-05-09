# https://www.acmicpc.net/problem/21276
import sys
si = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def find_root(x):
    if not ancestor[x]:
        return x
    
    if root[x] != '':
        return root[x]
    
    for nxt in ancestor[x]:
        ret = find_root(nxt)

    root[x] = ret    
    return ret

def go(x):
    child = []
    for nxt in tree[x]:
        for comp in tree[x]:
            if nxt == comp: continue
            if nxt in tree[comp]:
                break
        else:
            child.append(nxt)
            go(nxt)
    
    answer[x].append(str(len(child)))
    for c in child:
        answer[x].append(c)
    answer[x].sort()

if __name__ == '__main__':
    n = int(si())
    names = list(si().split())
    
    m = int(si())
    tree = dict()
    ancestor = dict()
    root = dict()
    answer = dict()
    for name in names:
        tree[name] = set()
        ancestor[name] = set()
        root[name] = ''
        answer[name] = []
    
    for _ in range(m):
        x, y = si().split()
        tree[y].add(x)
        ancestor[x].add(y)
    
    for name in names:
        find_root(name)
    
    cnt = 0
    ans = []
    for name in root:
        if root[name] == '':
            cnt += 1
            ans.append(name)

    ans.sort()
    print(cnt)
    print(*ans)
    for name in ans:
        go(name)
    
    for name in sorted(answer):
        print(f'{name} {" ".join(answer[name])}')