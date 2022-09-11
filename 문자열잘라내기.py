# https://www.acmicpc.net/problem/2866
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def deter(mid):
    tmp = set()
    
    for i in range(c):
        cur = ''.join(s[i][mid:])
        if cur in tmp:
            return False
        tmp.add(cur)
    return True

if __name__ == '__main__':
    r, c = mis()
    table = [si().strip() for _ in range(r)]
    
    s = list(zip(*table))
    
    left, right = 0, r - 1
    ans = 0
    while left <= right:
        mid = (left + right) // 2

        if not deter(mid):
            right = mid - 1
        else:
            left = mid + 1
            ans = mid
    print(ans)