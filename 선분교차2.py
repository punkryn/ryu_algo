# https://www.acmicpc.net/problem/17387
from sys import stdin

si = stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    s1 = x1 * y2 + x2 * y3 + x3 * y1
    s2 = x2 * y1 + x3 * y2 + x1 * y3
    res = s1 - s2
    if res > 0: return 1
    elif res < 0: return -1
    return 0

if __name__ == '__main__':
    x1, y1, x2, y2 = map(int, si().split())
    x3, y3, x4, y4 = map(int, si().split())

    op1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    op2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    if op1 == 0 and op2 == 0:
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and \
            min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            print(1)
        else:
            print(0)
    elif op1 <= 0 and op2 <= 0:
        print(1)
    else:
        print(0)