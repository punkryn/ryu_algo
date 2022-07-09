# https://www.acmicpc.net/problem/15961
import sys
from collections import defaultdict
si = sys.stdin.readline

if __name__ == '__main__':
    n, d, k, c = map(int, si().split())
    s = [int(si()) for _ in range(n)]
    
    cur = defaultdict(int)
    r = 0
    order = 0
    ans = 0
    for l in range(n):
        while order < k:
            cur[s[r]] += 1
            r = (r + 1) % n
            order += 1
        
        ans = max(ans, len(cur) + (1 if c not in cur else 0))
        order -= 1
        cur[s[l]] -= 1
        if cur[s[l]] == 0:
            del cur[s[l]]
    print(ans)