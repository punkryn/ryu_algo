# https://www.acmicpc.net/problem/1082
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    p = list(map(int, si().split()))
    m = int(si())

    dp = [[] for _ in range(m + 1)]
    dp[0].append('')
    
    for i in range(m):
        if not len(dp[i]): continue
        for j in range(n):
            tmp = p[j] + i
            if tmp > m: continue
            for k in dp[i]:
                string = ''
                if not len(k):
                    dp[tmp].append(str(j))
                else:
                    for l in range(len(k)):
                        if int(k[l]) <= j:
                            string += str(j)
                            string += k[l:]
                            break
                        else:
                            string += k[l]
                    
                    if not dp[tmp]:
                        dp[tmp].append(string)
                    else:
                        if int(dp[tmp][0]) < int(string):
                            dp[tmp][0] = string
    ans = 0
    for i in range(1, m + 1):
        for j in dp[i]:
            ans = max(ans, int(j))
    print(ans)