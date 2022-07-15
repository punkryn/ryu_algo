# https://www.acmicpc.net/problem/1301
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def go(x, y):
    if dp[ball[0]][ball[1]][ball[2]][ball[3]][ball[4]][x][y] != -1:
        return dp[ball[0]][ball[1]][ball[2]][ball[3]][ball[4]][x][y]
    
    if ball[0] + ball[1] + ball[2] + ball[3] + ball[4] == 0:
        return 1
    
    ret = 0
    for i in range(n):
        if ball[i] == 0: continue
        if x == i or y == i: continue
        ball[i] -= 1
        ret += go(y, i)
        ball[i] += 1
    dp[ball[0]][ball[1]][ball[2]][ball[3]][ball[4]][x][y] = ret
    return ret

if __name__ == '__main__':
    n = int(si())
    ball = [int(si()) for _ in range(n)]
    while len(ball) < 5:
        ball += [0]
    ans = 0
    dp = [[[[[[[-1] * 5 for _ in range(5)] for _ in range(11)] for __ in range(11)] for ___ in range(11)] for _ in range(11)] for _ in range(11)]
    for i in range(n):
        for j in range(n):
            if i == j: continue
            ball[i] -= 1
            ball[j] -= 1
            ans += go(i, j)
            ball[i] += 1
            ball[j] += 1
    print(ans)