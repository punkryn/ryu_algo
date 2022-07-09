# https://www.acmicpc.net/problem/17255
import sys
si = sys.stdin.readline

def dfs(s):
    L = set(list(s))
    if len(L) == 1:
        return 1
    
    ret = 0
    ret += dfs(s[1:])
    ret += dfs(s[:-1])
    return ret

if __name__ == '__main__':
    n = si().strip()
    print(dfs(n))