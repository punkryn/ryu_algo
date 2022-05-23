# https://www.acmicpc.net/problem/9328
from sys import stdin
from collections import deque
si = stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(gates, keys, h, w, MAP):
    q = deque(gates)
    visited = [[0] * w for _ in range(h)]

    find_gates(gates, MAP, w, h, keys)

    for x, y in gates:
        visited[x][y] = 1
    cnt = 0

    for i in range(w):
        if MAP[0][i] == '$':
            cnt += 1
        if MAP[h - 1][i] == '$':
            cnt += 1
    
    for i in range(1, h - 1):
        if MAP[i][0] == '$':
            cnt += 1
        if MAP[i][w - 1] == '$':
            cnt += 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < h and 0 <= ny < w) or visited[nx][ny]:
                continue
            if MAP[nx][ny] == '.':
                visited[nx][ny] = 1
                q.append((nx, ny))
            elif MAP[nx][ny] == '$':
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
            elif MAP[nx][ny] == '*':
                continue
            elif ord('A') <= ord(MAP[nx][ny]) <= ord('Z'):
                key = chr(ord(MAP[nx][ny]) + (ord('a') - ord('A')))
                if key in keys:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
            elif ord('a') <= ord(MAP[nx][ny]) <= ord('z'):
                keys.add(MAP[nx][ny])
                visited[nx][ny] = 1
                q.append((nx, ny))
    return cnt

def find_gates(gates, MAP, w, h, keys):
    for i in range(w):
        if ord('A') <= ord(MAP[0][i]) <= ord('Z'):
            key = chr(ord(MAP[0][i]) + (ord('a') - ord('A')))
            if key in keys:
                gates.add((0, i))
        
        if ord('A') <= ord(MAP[h - 1][i]) <= ord('Z'):
            key = chr(ord(MAP[h - 1][i]) + (ord('a') - ord('A')))
            if key in keys:
                gates.add((h - 1, i))
    
    for i in range(1, h - 1):
        if ord('A') <= ord(MAP[i][0]) <= ord('Z'):
            key = chr(ord(MAP[i][0]) + (ord('a') - ord('A')))
            if key in keys:
                gates.add((i, 0))
        
        if ord('A') <= ord(MAP[i][w - 1]) <= ord('Z'):
            key = chr(ord(MAP[i][w - 1]) + (ord('a') - ord('A')))
            if key in keys:
                gates.add((i, w - 1))

def main():
    h, w = map(int, si().split())
    MAP = [si().strip() for _ in range(h)]
    keys = si().strip()
    if keys == '0':
        keys = set()
    else:
        keys = set([k for k in keys])
    
    gates = set()
    ans = 0
    for i in range(w):
        if MAP[0][i] == '.':
            gates.add((0, i))
        if MAP[h - 1][i] == '.':
            gates.add((h - 1, i))

        if MAP[0][i] == '$':
            ans += 1
            gates.add((0, i))
            
        if MAP[h - 1][i] == '$':
            ans += 1
            gates.add((h - 1, i))

        if ord('a') <= ord(MAP[0][i]) <= ord('z'):
            gates.add((0, i))
            keys.add(MAP[0][i])
        
        if ord('a') <= ord(MAP[h - 1][i]) <= ord('z'):
            gates.add((h - 1, i))
            keys.add(MAP[h - 1][i])
    
    for i in range(1, h - 1):
        if MAP[i][0] == '.':
            gates.add((i, 0))
        if MAP[i][w - 1] == '.':
            gates.add((i, w - 1))

        if MAP[i][0] == '$':
            ans += 1
            gates.add((i, 0))
        
        if MAP[i][w - 1] == '$':
            ans += 1
            gates.add((i, w - 1))
        
        if ord('a') <= ord(MAP[i][0]) <= ord('z'):
            gates.add((i, 0))
            keys.add(MAP[i][0])
        
        if ord('a') <= ord(MAP[i][w - 1]) <= ord('z'):
            gates.add((i, w - 1))
            keys.add(MAP[i][w - 1])
    
    # find_gates(gates, MAP, w, h, keys)
    
    while True:
        key_cnt = len(keys)
        gate_cnt = len(gates)
        tmp = bfs(gates, keys, h, w, MAP)
        if ans == tmp and key_cnt == len(keys) and gate_cnt == len(gates):
            break

        ans = tmp
    print(ans)


if __name__ == '__main__':
    for _ in range(int(si())):
        main()