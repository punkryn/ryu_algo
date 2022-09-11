# https://www.acmicpc.net/problem/16507
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    r, c, q = mis()
    pixel = [list(mis()) for _ in range(r)]
    
    for i in range(r):
        for j in range(1, c):
            pixel[i][j] += pixel[i][j - 1]
    
    for i in range(c):
        for j in range(1, r):
            pixel[j][i] += pixel[j - 1][i]

    for _ in range(q):
        r1, c1, r2, c2 = mis()
        if r1 >= 2 and c1 >= 2:
            print((pixel[r2 - 1][c2 - 1] - (pixel[r2 - 1][c1 - 2] if c1 >= 2 else 0) - (pixel[r1 - 2][c2 - 1] if r1 >= 2 else 0) + pixel[r1 - 2][c1 - 2]) // ((r2 - r1 + 1) * (c2 - c1 + 1)))
        else:
            print((pixel[r2 - 1][c2 - 1] - (pixel[r2 - 1][c1 - 2] if c1 >= 2 else 0) - (pixel[r1 - 2][c2 - 1] if r1 >= 2 else 0)) // ((r2 - r1 + 1) * (c2 - c1 + 1)))