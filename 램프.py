# https://www.acmicpc.net/problem/1034
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n, m = mis()
    table = [si().strip() for _ in range(n)]
            
    k = int(si())

    ans = 0
    v = set()
    for row in table:
        if row in v:
            continue

        v.add(row)
        cnt = table.count(row)
        zero_cnt = row.count('0')
        if k >= zero_cnt and (k - zero_cnt) % 2 == 0:
            ans = max(ans, cnt)
    
    print(ans)