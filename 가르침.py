# https://www.acmicpc.net/problem/1062
import sys
from itertools import combinations
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n, k = mis()
    words = [si().strip() for _ in range(n)]
    
    if k < 5:
        print(0)
        exit()

    alpha = set([chr(ord('a') + i) for i in range(26)])
    alpha.remove('a')
    alpha.remove('n')
    alpha.remove('t')
    alpha.remove('i')
    alpha.remove('c')

    ans = 0
    for comb in combinations(alpha, k - 5):
        cnt = 0
        for word in words:
            for a in word[4:-4]:
                if a not in alpha: continue
                if a not in comb:
                    break
            else:
                cnt += 1
        
        ans = max(ans, cnt)
    print(ans)