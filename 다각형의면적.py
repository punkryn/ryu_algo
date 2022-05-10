# https://www.acmicpc.net/problem/2166
import sys
si = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    return ((x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)) / 2

if __name__ == '__main__':
    n = int(si())
    coord = [list(map(int, si().split())) for _ in range(n)]
    ans = 0
    for i in range(1, n):
        ans += ccw(coord[0][0], coord[0][1], coord[i - 1][0], coord[i - 1][1], coord[i][0], coord[i][1])
    print(f'{abs(ans):.1f}')