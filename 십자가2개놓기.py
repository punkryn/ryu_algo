# https://www.acmicpc.net/problem/17085
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def up(x, y, l):
    if x - l < 0:
        return False
    for i in range(x, x - l - 1, -1):
        if grid[i][y] == '.':
            return False
    return True

def down(x, y, l):
    if x + l >= n:
        return False
    
    for i in range(x, x + l + 1):
        if grid[i][y] == '.':
            return False
    return True

def left(x, y, l):
    if y - l < 0:
        return False
    
    for i in range(y, y - l - 1, -1):
        if grid[x][i] == '.':
            return False
    return True

def right(x, y, l):
    if y + l >= m:
        return False
    
    for i in range(y, y + l + 1):
        if grid[x][i] == '.':
            return False
    return True

if __name__ == '__main__':
    n, m = mis()
    grid = [si().strip() for _ in range(n)]
    coord = [[] for _ in range(8)]
    for i in range(8):
        for j in range(n):
            for k in range(m):
                if up(j, k, i) and down(j, k, i) and left(j, k, i) and right(j, k, i):
                    coord[i].append((j, k))
    
    ans = 0
    for i in range(7, -1, -1):
        for j in range(7, -1, -1):
            for x1, y1 in coord[i]:
                tmp = set()
                for k in range(x1, x1 - i - 1, -1):
                    tmp.add((k, y1))
                for k in range(x1, x1 + i + 1):
                    tmp.add((k, y1))
                for k in range(y1, y1 - i - 1, -1):
                    tmp.add((x1, k))
                for k in range(y1, y1 + i + 1):
                    tmp.add((x1, k))
                for x2, y2 in coord[j]:
                    if x1 == y2 and y1 == y2: continue
                    for k in range(x2, x2 - j - 1, -1):
                        if (k, y2) in tmp:
                            break
                    else:
                        for k in range(x2, x2 + j + 1):
                            if (k, y2) in tmp:
                                break
                        else:
                            for k in range(y2, y2 - j - 1, -1):
                                if (x2, k) in tmp:
                                    break
                            else:
                                for k in range(y2, y2 + j + 1):
                                    if (x2, k) in tmp:
                                        break
                                else:
                                    ans = max(ans, (4 * i + 1) * (4 * j + 1))
    print(ans)
