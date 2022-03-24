# https://www.acmicpc.net/problem/17610
import sys
si = sys.stdin.readline

def go(depth, v):
    if depth == k:
        print(v)
        if v < a:
            ans.add(v)
        return
    
    go(depth + 1, v)
    go(depth + 1, v + weights[depth])
    if v > weights[depth]:
        go(depth + 1, v - weights[depth])
    else:
        go(depth + 1, weights[depth] - v)

if __name__ == '__main__':
    k = int(si())
    weights = list(map(int, si().split()))
    a = sum(weights)
    ans = set()

    go(0, 0)
    print(a - len(ans))