# https://www.acmicpc.net/problem/1086
import sys
import math

si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    arr = [si().strip() for _ in range(n)]
    k = int(si())

    cache = [0] * 51
    cache[0] = 1
    for i in range(1, 51):
        cache[i] = (cache[i - 1] * 10) % k
    
    strlen = [0] * n
    for i in range(n):
        strlen[i] = int(arr[i]) % k

    dp = [[0] * k for _ in range(1 << n)]
    dp[0][0] = 1
    for i in range(1 << n):
        for j in range(n):
            if (i & (1 << j)) == 0:
                nxt = i | (1 << j)
                for l in range(k):
                    nxtk = ((l * cache[len(arr[j])]) % k + strlen[j]) % k
                    dp[nxt][nxtk] += dp[i][l]
    
    total = 1
    for i in range(2, n + 1):
        total *= i
    
    cur = dp[(1 << n) - 1][0]
    MOD = math.gcd(total, cur)
    print(f'{cur // MOD}/{total // MOD}')