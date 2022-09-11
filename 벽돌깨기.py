# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo
# import sys
# from itertools import permutations
from collections import deque
si = input
mis = lambda: map(int, si().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def permutations(n, cur=[]):
    global per
    if n == 0:
        per.append(cur[:])
        return
    
    for i in range(w):
        cur.append(i)
        permutations(n - 1, cur)
        cur.pop()

def fall(grid):
    for i in range(h - 2, -1, -1):
        for j in range(w):
            if grid[i][j] != 0:
                idx = i
                while idx + 1 < h and grid[idx + 1][j] == 0:
                    idx += 1
                
                if idx != i:
                    grid[idx][j] = grid[i][j]
                    grid[i][j] = 0

def brick_break(order, grid):
    for o in order:
        q = deque()
        for i in range(h):
            if grid[i][o] != 0:
                q.append((i, o))
                break
        
        while q:
            x, y = q.popleft()
            cnt = grid[x][y]
            grid[x][y] = 0
            
            x_ = x
            for i in range(cnt - 1):
                if x_ == 0: break
                x_ -= 1
                if grid[x_][y] != 0:
                    q.append((x_, y))
            
            y_ = y
            for i in range(cnt - 1):
                if y_ == w - 1: break
                y_ += 1
                if grid[x][y_] != 0:
                    q.append((x, y_))
            
            x_ = x
            for i in range(cnt - 1):
                if x_ == h - 1: break
                x_ += 1
                if grid[x_][y] != 0:
                    q.append((x_, y))
            
            y_ = y
            for i in range(cnt - 1):
                if y_ == 0: break
                y_ -= 1
                if grid[x][y_] != 0:
                    q.append((x, y_))
        
        fall(grid)
    total = len([grid[i][j] for i in range(h) for j in range(w) if grid[i][j] != 0])
    return total
            
            

if __name__ == '__main__':
    for test_case in range(1, int(si()) + 1):
        n, w, h = mis()
        grid = [list(mis()) for _ in range(h)]
        

        ans = float('inf')
        per = []
        permutations(n)
        for comb in per:
            grid_ = [row[:] for row in grid]
            ans = min(ans, brick_break(comb, grid_))
        print(f'#{test_case} {ans}')