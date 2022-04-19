# https://www.acmicpc.net/problem/16435
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, l = map(int, si().split())
    h = sorted(list(map(int, si().split())))
    for i in h:
        if l >= i:
            l += 1
        else:
            break
    print(l)