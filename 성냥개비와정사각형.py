# https://www.acmicpc.net/problem/2214
import sys
si = sys.stdin.readline

def up(x, y, l):
    for i in range(y, y + l):
        if not (s[x][i] & 1):
            return False
    return True

def down(x, y, l):
    for i in range(y, y + l):
        if not (s[x + l - 1][i] & (1 << 2)):
            return False
    return True

def right(x, y, l):
    for i in range(x, x + l):
        if not (s[i][y + l - 1] & (1 << 1)):
            return False
    return True

def left(x, y, l):
    for i in range(x, x + l):
        if not (s[i][y] & (1 << 3)):
            return False
    return True

if __name__ == '__main__':
    while True:
        r, c = map(int, si().split())
        if r == 0 and c == 0:
            break
        p = [si().strip() for _ in range(2 * r + 1)]
        s = [[0] * c for _ in range(r)]
        for i in range(1, 2 * r + 1, 2):
            x = i // 2
            for j in range(c):
                tmp = 0
                if p[i - 1][j] != '*':
                    tmp += (1 << 0)
                if p[i + 1][j] != '*':
                    tmp += (1 << 2)
                if p[i][j] != '*':
                    tmp += (1 << 3)
                if p[i][j + 1] != '*':
                    tmp += (1 << 1)

                s[x][j] = tmp
        
        ans = 0
        for i in range(1, min(r, c) + 1):
            for j in range(r - i + 1):
                for k in range(c - i + 1):
                    if up(j, k, i) and down(j, k, i) and right(j, k, i) and left(j, k, i):
                        ans += 1
        print(f'{ans} squares')