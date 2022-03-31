# https://www.acmicpc.net/problem/5549
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())
    k = int(si())
    MAP = [si().strip() for _ in range(n)]
    
    jungle = [[0] * (m + 1) for _ in range(n + 1)]
    ocean = [[0] * (m + 1) for _ in range(n + 1)]
    ice = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            jungle[i][j] = jungle[i - 1][j] + jungle[i][j - 1] - jungle[i - 1][j - 1] + (1 if MAP[i - 1][j- 1] == 'J' else 0)
            ocean[i][j] = ocean[i - 1][j] + ocean[i][j - 1] - ocean[i - 1][j - 1] + (1 if MAP[i-1][j-1] == 'O' else 0)
            ice[i][j] = ice[i - 1][j] + ice[i][j - 1] - ice[i - 1][j - 1] + (1 if MAP[i-1][j - 1] == 'I' else 0)

    for _ in range(k):
        a, b, c, d = map(int, si().split())
        j = jungle[c][d] - jungle[a - 1][d] - jungle[c][b - 1] + jungle[a - 1][b - 1]
        o = ocean[c][d] - ocean[a - 1][d] - ocean[c][b - 1] + ocean[a - 1][b - 1]
        i = ice[c][d] - ice[a - 1][d] - ice[c][b - 1] + ice[a - 1][b - 1]
        print(j, o, i)