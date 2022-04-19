# https://www.acmicpc.net/problem/1007
import sys
import math
si = sys.stdin.readline

def go(depth, curx, cury, prev):
    global v
    if depth == 0:
        nx = x_total - curx
        ny = y_total - cury
        v = min(v, math.sqrt((curx - nx) ** 2 + (cury - ny) ** 2))
        return
    
    for i in range(prev + 1, n - depth + 1):
        go(depth - 1, curx + coord[i][0], cury + coord[i][1], i)
        

if __name__ == '__main__':
    ans = []
    for _ in range(int(si())):
        n = int(si())
        x_total = 0
        y_total = 0
        coord = []
        for __ in range(n):
            x, y = map(int, si().split())
            coord.append((x, y))
            x_total += x
            y_total += y
        
        v = 1e9
        go(n // 2, 0, 0, -1)
        ans.append(v)
    for a in ans:
        print(a)