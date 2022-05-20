# https://www.acmicpc.net/problem/9328
from sys import stdin
si = stdin.raedline

def bfs(gates, keys):
    

def main():
    h, w = map(int, si().split())
    MAP = [si().strip() for _ in range(h)]
    keys = si().strip()
    if keys == '0':
        keys = set()
    else:
        keys = set([k for k in keys])
    
    gates = []
    for i in range(w):
        if MAP[0][i] == '.':
            gates.append((0, i))
        if MAP[h - 1][i] == '.':
            gates.append((h - 1, i))
    
    for i in range(1, h - 1):
        if MAP[i][0] == '.':
            gates.append((i, 0))
        if MAP[i][w - 1] == '.':
            gates.append((i, w - 1))
    



if __name__ == '__main__':
    for _ in range(int(si())):
        main()