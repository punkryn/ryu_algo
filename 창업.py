# https://www.acmicpc.net/problem/16890
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    g = list(si().strip())
    q = list(si().strip())
    g.sort()
    q.sort(reverse=True)
    print(g)
    print(q)
    n = len(q)
    ks, ke = 0, (n + 1) // 2 - 1
    cs, ce = 0, n // 2 - 1
    if ke < 0: ke = 0
    if ce < 0: ce = 0
    turn = True
    ans = ['' for _ in range(len(q))]

    rs, re = 0, n - 1
    for i in range(n):
        if turn:
            if g[ks] < q[cs]: 
                ans[rs] = g[ks]
                rs += 1
                ks += 1
            else:
                ans[re] = g[ke]         
                re -= 1
                ke -= 1
        else:
            if g[ks] < q[cs]:
                ans[rs] = q[cs]
                rs += 1
                cs += 1
            else:
                ans[re] = q[ce]
                re -= 1
                ce -= 1
        
        turn = not turn

    print(''.join(ans))