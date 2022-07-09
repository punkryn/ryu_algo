# https://www.acmicpc.net/problem/11444
MOD = 1000000007
def op(a, b):
    c = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] += (a[i][k] * b[k][j]) % MOD
            c[i][j] %= MOD
    return c

if __name__ == '__main__':
    n = int(input())
    
    ans = [[1, 0], [0, 1]]
    a = [[1, 1], [1, 0]]

    while n:
        if n % 2 == 1:
            ans = op(ans, a)
        a = op(a, a)
        n //= 2
    print(ans[0][1])