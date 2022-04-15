# https://www.acmicpc.net/problem/16953
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())

    cnt = 1
    while n < m:
        if m % 10 == 1:
            m //= 10
            cnt += 1
        elif m % 2 == 0:
            m //= 2
            cnt += 1
        else:
            print(-1)
            exit()
    
    if n == m:
        print(cnt)
    else:
        print(-1)