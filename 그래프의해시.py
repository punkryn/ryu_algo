# https://www.acmicpc.net/problem/2328
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    matrix = [list(map(int, si().split())) for _ in range(n)]
    s, e = 0, 1
