# https://www.acmicpc.net/problem/17779
import sys
si = sys.stdin.readline

def calc(x, y, d1, d2):
    a1 = a2 = a3 = a4 = a5 = 0
    tmp = [[0] * n for _ in range(n)]
    tmp[x][y] = 5
    nx, ny = x, y
    for _ in range(d1):
        nx += 1
        ny -= 1
        tmp[nx][ny] = 5
    nx, ny = x, y
    for _ in range(d2):
        nx += 1
        ny += 1
        tmp[nx][ny] = 5
    nx, ny = x + d1, y - d1
    for _ in range(d2):
        nx += 1
        ny += 1
        tmp[nx][ny] = 5
    nx, ny = x + d2, y + d2
    for _ in range(d1):
        nx += 1
        ny -= 1
        tmp[nx][ny] = 5
    flag = False
    for i in range(n):
        s, e, flag = 0, 0, False
        for j in range(n):
            if tmp[i][j] == 5:
                s = j
                flag = True
                break
        for j in range(n - 1, -1, -1):
            if tmp[i][j] == 5:
                e = j
                break
        if flag:
            for j in range(s, e + 1):
                tmp[i][j] = 5
    
    # print(x, y, d1, d2)
    # for t in tmp:
    #     print(t)

    for i in range(n):
        for j in range(n):
            if tmp[i][j] == 0:
                if i < x + d1 and j <= y: a1 += p[i][j]
                elif i <= x + d2 and y < j < n: a2 += p[i][j]
                elif x + d1 <= i < n and j < y - d1 + d2: a3 += p[i][j]
                elif x + d2 < i < n and y - d1 + d2 <= j < n: a4 += p[i][j]
            elif tmp[i][j] == 5:
                a5 += p[i][j]
    
    return max(a1, a2, a3, a4, a5) - min(a1, a2, a3, a4, a5)

if __name__ == '__main__':
    n = int(si())
    p = [list(map(int, si().split())) for _ in range(n)]
    ans = int(1e9)
    for i in range(n):
        for j in range(n):
            for d1 in range(1, n):
                for d2 in range(1, n):
                    if i + d1 + d2 < n and 0 <= j - d1 and j + d2 < n:
                        ans = min(ans, calc(i, j, d1, d2))
                    else:
                        break
    print(ans)