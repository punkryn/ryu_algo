# https://www.acmicpc.net/problem/9527
from sys import stdin

si = stdin.readline

def calc(x):
    ans = x & 1
    for i in range(54, 0, -1):
        if x & (1 << i):
            ans += ps[i - 1] + (x - (1 << i) + 1)
            x -= 1 << i
    return ans

if __name__ == '__main__':
    a, b = map(int, si().split())
    ps = [0] * 100
    ps[0] = 1
    for i in range(1, 100):
        ps[i] = ps[i - 1] * 2 + (1 << i)
    print(calc(b) - calc(a - 1))