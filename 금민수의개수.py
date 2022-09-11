# https://www.acmicpc.net/problem/1527
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    a, b = mis()
    dp = [set() for _ in range(11)]
    dp[0].add('')
    
    for i in range(1, 11):
        for prev in dp[i - 1]:
            dp[i].add(prev + '4')
            dp[i].add(prev + '7')
    
    ans = 0
    for i in range(len(str(a)), len(str(b)) + 1):
        for p in dp[i]:
            if a <= int(p) <= b:
                ans += 1
    print(ans)