# https://www.acmicpc.net/problem/16438
import sys
si = sys.stdin.readline

def daq(start, end, depth):
    global cnt
    if start >= end or depth == 7:
        return
    
    cnt = max(cnt, depth)

    mid = (start + end) // 2
    for i in range(start, end + 1):
        if i <= mid: ans[depth][i] = 'A'
        else: ans[depth][i] = 'B'
    
    daq(start, mid, depth + 1)
    daq(mid + 1, end, depth + 1)

if __name__ == '__main__':
    n = int(si())
    ans = [['' for _ in range(n + 1)] for _ in range(8)]
    cnt = 0
    daq(1, n, 0)

    for i in range(cnt + 1):
        for j in range(1, n + 1):
            if ans[i][j] == '':
                if j % 2 == 1:
                    ans[i][j] = 'A'
                else:
                    ans[i][j] = 'B'

    tmp = 'B' + 'A' * (n - 1)
    for i in range(7):
        if ans[i][1] == '':
            print(tmp)
        else:
            print(''.join(ans[i]))