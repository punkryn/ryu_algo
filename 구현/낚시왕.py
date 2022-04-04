# https://www.acmicpc.net/problem/17143
from logging import exception
import sys
si = sys.stdin.readline

UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4

def catch_shark(col):
    size = 0
    for row in range(1, r + 1):
        if grid[row][col]:
            _, _, z = grid[row][col].pop()
            size += z
            break
    return size

def move():
    q = []
    for pos in shark_pos:
        r_, c_, s_, d_, z_ = pos
        if grid[r_][c_]:
            grid[r_][c_].pop()
        if d_ == LEFT:
            if s_ < c_:
                q.append([r_, c_ - s_, s_, d_, z_])
            else:
                dist = s_ - (c_ - 1)
                mok = dist // (c - 1)
                dist -= (c - 1) * mok
                if mok % 2 == 0:
                    d_ = RIGHT
                    cur = [r_, dist + 1, s_, d_, z_]
                    q.append(cur)
                else:
                    cur = [r_, c - dist, s_, d_, z_]
                    q.append(cur)
        elif d_ == RIGHT:
            if c - c_ >= s_:
                q.append([r_, c_ + s_, s_, d_, z_])
            else:
                dist = s_ - (c - c_)
                mok = dist // (c - 1)
                dist -= (c - 1) * mok
                if mok % 2 == 0:
                    d_ = LEFT
                    cur = [r_, c - dist, s_, d_, z_]
                    q.append(cur)
                else:
                    cur = [r_, dist + 1, s_, d_, z_]
                    q.append(cur)
        elif d_ == UP:
            if s_ < r_:
                q.append([r_ - s_, c_, s_, d_, z_])
            else:
                dist = s_ - (r_ - 1)
                mok = dist // (r - 1)
                dist -= (r - 1) * mok
                if mok % 2 == 0:
                    d_ = DOWN
                    cur = [dist + 1, c_, s_, d_, z_]
                    q.append(cur)
                else:
                    cur = [r - dist, c_, s_, d_, z_]
                    q.append(cur)
        elif d_ == DOWN:
            if r - r_ >= s_:
                q.append([r_ + s_, c_, s_, d_, z_])
            else:
                dist = s_ - (r - r_)
                mok = dist // (r - 1)
                dist -= (r - 1) * mok
                if mok % 2 == 0:
                    d_ = UP
                    cur = [r - dist, c_, s_, d_, z_]
                    q.append(cur)
                else:
                    cur = [dist + 1, c_, s_, d_, z_]
                    q.append(cur)
    
    for cur in q:
        r_, c_, s_, d_, z_ = cur

        if not grid[r_][c_]:
            grid[r_][c_].append([s_, d_, z_])
        else:
            if grid[r_][c_][0][2] < z_:
                grid[r_][c_].pop()
                grid[r_][c_].append([s_, d_, z_])
        
                

def find_shark(q):
    q = []
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if grid[i][j]:
                s_, d_, z_ = grid[i][j][0]
                q.append([i, j, s_, d_, z_])
    return q

if __name__ == '__main__':
    r, c, m = map(int, si().split())
    grid = [[[] for _ in range(c + 2)] for _ in range(r + 2)]
    shark_pos = []
    for _ in range(m):
        r_, c_, s_, d_, z_ = map(int, si().split())
        grid[r_][c_].append([s_, d_, z_])
        shark_pos.append([r_, c_, s_, d_, z_])

    ans = 0
    for i in range(1, c + 1):
        ans += catch_shark(i)
        shark_pos = find_shark(shark_pos)
        move()
        shark_pos = find_shark(shark_pos)
        
    print(ans)