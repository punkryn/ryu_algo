# https://www.acmicpc.net/problem/14939
from sys import stdin
si = stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def find_nxt(state):
    cand = []
    for i in range(10):
        for j in range(10):
            cnt = 1 if state[i] & (1 << j) else 0
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if not (0 <= ni < 10 and 0 <= nj < 10): continue
                if state[ni] & (1 << nj):
                    cnt += 1
            if cnt > 2:
                cand.append((i, j))
    return cand

def click(x, y, state):
    state[x] ^= (1 << y)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < 10 and 0 <= ny < 10):
            continue
        
        state[nx] ^= (1 << ny)
    return state

def go(depth, state):
    global ans
    cand = find_nxt(state)
    if len(cand) == 0:
        ans = min(ans, depth)
        return
    
    for x, y in cand:
        tmp = state[:]
        click(x, y, state)
        go(depth + 1, state)
        state = tmp
    go(depth + 1, state)

if __name__ == '__main__':
    a = [si().strip() for _ in range(10)]
    state = [0] * 10
    ans = int(1e9)
    go(0, state)
    if ans == int(1e9):
        print(-1)
    else:
        print(ans)