# https://www.acmicpc.net/problem/14502
import sys
from collections import deque
import copy
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(map_, cand, virus, n, m):
    q = deque()
    for c in cand:
        map_[c[0]][c[1]] = '1'
    for v in virus:
        q.append(v)
    while q:
        cur = q.popleft()
        x, y = cur
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if map_[nx][ny] != '0': continue
                map_[nx][ny] = '2'
                q.append((nx, ny))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if map_[i][j] == '0':
                cnt += 1
    return cnt

def go(blank, depth, cand, MAP, prev, virus, n, m):
    if depth == 3:
        map_ = copy.deepcopy(MAP)
        return bfs(map_, cand, virus, n, m)
    
    space = 0
    for i in range(prev + 1, len(blank)):
        cand.append(blank[i])
        space = max(space, go(blank, depth + 1, cand, MAP, i, virus, n, m))
        cand.pop()
    return space

def main():
    n, m = map(int, si().split())
    MAP = [list(si().split()) for _ in range(n)]
    blank = [(i, j) for i in range(n) for j in range(m) if MAP[i][j] == '0']
    virus = [(i, j) for i in range(n) for j in range(m) if MAP[i][j] == '2']
    print(go(blank, 0, [], MAP, -1, virus, n, m))

if __name__ == '__main__':
    main()