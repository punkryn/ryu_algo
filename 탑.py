# https://www.acmicpc.net/problem/2493
import sys
sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())
    top = list(mis())
    
    stack = []
    ans = []
    for i in range(n):
        while stack and stack[-1][1] < top[i]:
            stack.pop()
        
        if not stack:
            stack.append((i, top[i]))
            ans.append(0)
            continue
        
        ans.append(stack[-1][0] + 1)
        stack.append((i, top[i]))
    print(*ans)