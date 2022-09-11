# https://www.acmicpc.net/problem/16927
import sys
sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def get_nxt_pos(x, y, r, rx, ry, cx, cy):
    while r:
        if x == rx and y == cx:
            if ry - rx < r:
                x += (ry - rx)
                r -= ry - rx
            else:
                x += r
                r = 0
        elif x == ry and y == cx:
            if cy - cx < r:
                y += (cy - cx)
                r -= (cy - cx)
            else:
                y += r
                r = 0
        elif x == ry and y == cy:
            if ry - rx < r:
                x -= (ry - rx)
                r -= ry - rx
            else:
                x -= r
                r = 0
        elif x == rx and y == cy:
            if cy - cx < r:
                y -= (cy - cx)
                r -= cy - cx
            else:
                y -= r
                r = 0
        # 5
        elif y == cx:
            if ry - x < r:
                r -= ry - x
                x += (ry - x)
            else:
                x += r
                r = 0
        # 6
        elif x == ry:
            if cy - y < r:
                r -= cy - y
                y += cy - y
            else:
                y += r
                r = 0
        # 7
        elif y == cy:
            if x - rx < r:
                r -= x - rx
                x -= x - rx
            else:
                x -= r
                r = 0
        # 8
        else:
            if y - cx < r:
                r -= y - cx
                y -= y - cx
            else:
                y -= r
                r = 0
    return (x, y)

if __name__ == '__main__':
    n, m, r = mis()
    a = [list(mis()) for _ in range(n)]

    rx, ry, cx, cy = 0, n - 1, 0, m - 1
    ans = [[0] * m for _ in range(n)]
    while rx < ry and cx < cy:
        r_ = r % ((ry - rx + cy - cx) * 2)
        
        for x in range(rx, ry):
            nx, ny = get_nxt_pos(x, cx, r_, rx, ry, cx, cy)
            ans[nx][ny] = a[x][cx]

        for y in range(cx, cy):
            nx, ny = get_nxt_pos(ry, y, r_, rx, ry, cx, cy)
            ans[nx][ny] = a[ry][y]
        
        for x in range(ry, rx, -1):
            nx, ny = get_nxt_pos(x, cy, r_, rx, ry, cx, cy)
            ans[nx][ny] = a[x][cy]
        
        for y in range(cy, cx, -1):
            nx, ny = get_nxt_pos(rx, y, r_, rx, ry, cx, cy)
            ans[nx][ny] = a[rx][y]
        
        rx += 1
        ry -= 1
        cx += 1
        cy -= 1

    for row in ans:
        print(*row)