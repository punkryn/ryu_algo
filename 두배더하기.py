# https://www.acmicpc.net/problem/12931
import sys
si = sys.stdin.readline

def make_even():
    cnt = 0
    for i in range(n):
        if b[i] % 2 == 1:
            b[i] -= 1
            cnt += 1
    return cnt

def isAllZero():
    for i in range(n):
        if b[i] != 0:
            return False
    return True

if __name__ == '__main__':
    n = int(si())
    b = list(map(int, si().split()))

    ans = 0
    while True:
        if isAllZero():
            break

        cnt = make_even()
        if cnt:
            ans += cnt
        else:
            ans += 1
            for i in range(n):
                b[i] //= 2
    print(ans)