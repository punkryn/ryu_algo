# https://www.acmicpc.net/problem/1509
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    s = si().rstrip()
    ls = len(s)
    if ls == 1:
        print(1)
        exit()
    p = [[False] * ls for _ in range(ls)]
    for i in range(ls):
        p[i][i] = True
    
    if ls >= 2:
        for i in range(ls - 1):
            if s[i] == s[i + 1]:
                p[i][i + 1] = True
    
    if ls >= 3:
        i, j = 0, 2
        while j < ls:
            i_, j_ = i, j
            while j_ < ls:
                if s[i_] == s[j_] and p[i_ + 1][j_ - 1]:
                    p[i_][j_] = True
                j_ += 1
                i_ += 1
                
            i = 0
            j += 1
    
    dp = [0] * ls
    for end in range(ls):
        dp[end] = int(1e6)
        for start in range(end + 1):
            if p[start][end]:
                if start == 0:
                    dp[end] = 1
                else:
                    dp[end] = min(dp[end], dp[start - 1] + 1)
    print(dp[ls - 1])