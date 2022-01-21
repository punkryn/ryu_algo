import sys
si = sys.stdin.readline

def main():
    k = int(si())
    a = [0] + list(map(int, si().split()))
    
    sum_ = [[0] * (k + 1) for _ in range(k + 1)]
    dp = [[0] * (k + 1) for _ in range(k + 1)]
    
    for i in range(k + 1):
        for j in range(i, k + 1):
            sum_[i][j] = sum_[i][j-1] + a[j]
    
    for length in range(2, k + 1):
        for i in range(1, k - length + 2):
            j = i + length - 1
            dp[i][j] = 500 * 500 * 10000
            for p in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][p] + dp[p+1][j] + sum_[i][j])
    print(dp[1][k])

if __name__ == '__main__':
    T = int(si())
    for _ in range(T):
        main()