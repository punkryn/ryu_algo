# https://www.acmicpc.net/problem/1022
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def left(n):
    return 1 + 4 * (n ** 2) + abs(n)

def right(n):
    return 1 + 4 * (n ** 2) - 3 * abs(n)

def up(n):
    return 1 + 4 * (n ** 2) - abs(n)

def down(n):
    return 1 + 4 * (n ** 2) + 3 * abs(n)

def getNum(r1, c1):
    if r1 < 0:
        cur = up(r1)
        if abs(c1) <= abs(r1):
            # -3 -3
            if c1 < 0:
                cur += abs(c1)
            # -3 3
            else:
                cur -= abs(c1)
        else:
            # -2 -3
            if c1 < 0:
                cur += abs(r1)
                cur += left(c1) - left(r1)
            # -2 3
            else:
                cur -= abs(r1)
                cur += right(c1) - right(r1)
        
    else:
        cur = down(r1)
        if c1 > 0:
            # 3 4 / 3 3
            if abs(c1) <= abs(r1) + 1:
                cur += abs(c1)
            # 1 3
            else:
                cur += abs(r1) + 1
                cur += right(c1) - right(r1 + 1)
        else:
            # 3 -3
            if abs(c1) <= abs(r1):
                cur -= abs(c1)
            # 2 -3
            else:
                cur -= abs(r1)
                cur += left(c1) - left(r1)

    return cur

if __name__ == '__main__':
    r1, c1, r2, c2 = mis()

    ans = []
    length = 0
    for i in range(r1, r2 + 1):
        cur = []
        for j in range(c1, c2 + 1):
            num = getNum(i, j)
            length = max(length, len(str(num)))
            cur.append(str(num))
        ans.append(cur)
    
    for d in ans:
        for num in d:
            if len(num) < length:
                print(' ' * (length - len(num)) + num, end=' ')
            else:
                print(num, end=' ')
        print()