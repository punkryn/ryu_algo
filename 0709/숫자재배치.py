# https://www.acmicpc.net/problem/16943
import sys
si = sys.stdin.readline
a, b = map(int, si().split())
l = list(str(a))
used = [False] * len(l)
ll = str(b)
ans = -1

def go(depth, cur=[]):
    global ans
    if depth == len(l):
        if int(''.join(cur)) < b:
            ans = max(ans, int(''.join(cur)))
        return
    
    for i in range(len(l)):
        if depth == 0 and int(l[i]) == 0: continue
        if used[i]: continue
        cur.append(l[i])
        used[i] = True
        go(depth + 1, cur)
        used[i] = False
        cur.pop()

if len(l) > len(ll):
    print(-1)
elif len(l) < len(ll):
    print(int(''.join(sorted(l, reverse=True))))
else:
    go(0)
    print(ans)