# https://www.acmicpc.net/problem/12026
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    block = si()

    dp = [-1] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            if block[i] == 'J':
                if block[j] == 'O' and dp[j] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[j] + (i - j) ** 2
                        continue
                    dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
            elif block[i] == 'O':
                if block[j] == 'B' and dp[j] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[j] + (i - j) ** 2
                    dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
            else:
                if block[j] == 'J' and dp[j] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[j] + (i - j) ** 2
                        continue
                    dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
    
    print(dp[-1])
            
if __name__ == '__main__':
    main()