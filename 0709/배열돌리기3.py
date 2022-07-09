# https://www.acmicpc.net/problem/16935
import sys
si = sys.stdin.readline

def op1():
    global a
    m = len(a[0])
    n = len(a)
    arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr[n - i - 1][j] = a[i][j]
    a = arr

def op2():
    global a
    m = len(a[0])
    n = len(a)
    arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr[i][m - j - 1] = a[i][j]
    a = arr

def op3():
    global a
    m = len(a[0])
    n = len(a)
    arr = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            arr[j][n - i - 1] = a[i][j]
    a = arr

def op4():
    global a
    m = len(a[0])
    n = len(a)
    arr = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            arr[m - j - 1][i] = a[i][j]
    a = arr

def op5():
    global a
    m = len(a[0])
    n = len(a)
    arr = [[0] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            arr[i][j + m // 2] = a[i][j]
    
    for i in range(n // 2):
        for j in range(m // 2, m):
            arr[i + n // 2][j] = a[i][j]
    
    for i in range(n // 2, n):
        for j in range(m // 2, m):
            arr[i][j - m // 2] = a[i][j]
    
    for i in range(n // 2, n):
        for j in range(m // 2):
            arr[i - n // 2][j] = a[i][j]
    a = arr

def op6():
    global a
    m = len(a[0])
    n = len(a)
    arr = [[0] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            arr[i + n // 2][j] = a[i][j]
    
    for i in range(n // 2):
        for j in range(m // 2, m):
            arr[i][j - m // 2] = a[i][j]
    
    for i in range(n // 2, n):
        for j in range(m // 2, m):
            arr[i - n // 2][j] = a[i][j]
    
    for i in range(n // 2, n):
        for j in range(m // 2):
            arr[i][j + m // 2] = a[i][j]
    a = arr


if __name__ == '__main__':
    n, m, r = map(int, si().split())
    a = [list(map(int, si().split())) for _ in range(n)]
    op = {1: op1, 2: op2, 3: op3, 4: op4, 5: op5, 6: op6}
    
    for o in map(int, si().split()):
        op[o]()
    
    for d in a:
        print(*d)