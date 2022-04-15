# https://www.acmicpc.net/problem/10216
import sys
si = sys.stdin.readline

dx = [-1, 0, 1, 0, 0]
dy = [0, 1, 0, -1, 0]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def main():
    n = int(si())
    a = [list(map(int, si().split())) for _ in range(n)]
    parent = [i for i in range(n)]
    ans = n
    for i in range(n - 1):
        x, y, r = a[i]
        for j in range(i + 1, n):
            x_, y_, r_ = a[j]
            if (x - x_) ** 2 + (y - y_) ** 2 <= (r + r_) ** 2:
                if find_parent(parent, i) != find_parent(parent, j):
                    union(parent, i, j)
                    ans -= 1
    print(ans)

if __name__ == '__main__':
    for _ in range(int(si())):
        main()