# https://www.acmicpc.net/problem/16987
import sys
si = sys.stdin.readline

def go(depth):
    global ans
    if depth == n:
        tot = 0
        for i in range(n):
            if eggs[i][0] <= 0:
                tot += 1
        ans = max(ans, tot)
        return
    
    if eggs[depth][0] <= 0:
        go(depth + 1)
        return

    flag = False
    for i in range(n):
        if i == depth or eggs[i][0] <= 0: continue
        flag = True
        eggs[depth][0] -= eggs[i][1]
        eggs[i][0] -= eggs[depth][1]
        go(depth + 1)
        eggs[i][0] += eggs[depth][1]
        eggs[depth][0] += eggs[i][1]
    if not flag:
        go(depth + 1)

if __name__=='__main__':
    n = int(si())
    eggs = [list(map(int, si().split())) for _ in range(n)]

    ans = 0
    go(0)
            
    print(ans)