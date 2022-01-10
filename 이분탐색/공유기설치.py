# https://www.acmicpc.net/problem/2110
import sys
n, c = map(int, sys.stdin.readline().split())
home = [int(sys.stdin.readline()) for _ in range(n)]
home.sort()

start = 0
end = home[-1] - home[0]

def deter(mid):
    cnt = 1
    cur = home[0]
    for idx in range(1, n):
        if home[idx] - cur >= mid:
            cnt += 1
            cur = home[idx]
        
        if cnt == c:
            break
    
    # print(cnt)
    return cnt >= c

ans = 0
while start <= end:
    mid = (start + end) // 2
    # print(start, end, mid)
    if deter(mid):
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)