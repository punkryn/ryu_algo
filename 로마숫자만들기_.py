# https://www.acmicpc.net/problem/16922
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def go(depth, k, cur=0, tmp=[]):
    if depth == n:
        print(tmp)
        ans.add(cur)
        return
    
    for i in range(k, 4):
        tmp.append(i)
        go(depth + 1, i, cur + x[i])
        tmp.pop()

if __name__ == '__main__':
    n = int(si())
    x = [1, 5, 10, 50]
    
    ans = set()
    go(0, 0)
    print(len(ans))