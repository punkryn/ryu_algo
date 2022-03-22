# https://www.acmicpc.net/problem/9019
import sys
from collections import deque
si = sys.stdin.readline

def D(a):
    a = a * 2
    return a % 10000

def S(a):
    a -= 1
    if a == -1:
        return 9999
    return a

def L(a):
    f = a // 1000
    a = (a - f * 1000) * 10 + f
    return a

def R(a):
    l = a % 10
    a = (a - l) // 10 + l * 1000
    return a

def main():
    a, b = map(int, si().split())
    
    q = deque()
    q.append((a, ''))
    visited = [0] * 10000
    visited[a] = 1
    while q:
        cur, hist = q.popleft()

        res = D(cur)
        if res == b:
            print(hist + 'D')
            return
        elif visited[res] == 0:
            visited[res] = 1
            q.append((res, hist + 'D'))
        res = S(cur)
        if res == b:
            print(hist + 'S')
            return
        elif visited[res] == 0:
            visited[res] = 1
            q.append((res, hist + 'S'))

        if not hist or hist[-1] != 'R':
            res = L(cur)
            if res == b:
                print(hist + 'L')
                return
            elif visited[res] == 0:
                visited[res] = 1
                q.append((res, hist + 'L'))
        if not hist or hist[-1] != 'L':
            res = R(cur)
            if res == b:
                print(hist + 'R')
                return
            elif visited[res] == 0:
                visited[res] = 1
                q.append((res, hist + 'R'))
    
if __name__ == '__main__':
    for _ in range(int(si())):
        main()