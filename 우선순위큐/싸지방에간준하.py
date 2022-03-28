# https://www.acmicpc.net/problem/12764
import sys
import heapq
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    times = [list(map(int, si().split())) for _ in range(n)]
    ps = [0] * (1000005)
    trace = [[0, 0, 0] for _ in range(1000005)]
    for time in times:
        s, e = time
        ps[s] += 1
        ps[e + 1] -= 1
        trace[s][0] = 1
        trace[s][2] = e
        trace[e][0] = 2
    
    x = 0
    for i in range(1000004):
        ps[i + 1] += ps[i]
        x = max(x, ps[i + 1])
    
    q = []
    for i in range(x):
        heapq.heappush(q, i)
    
    ans = [0] * x
    for i in range(1000004):
        if trace[i][0] == 1:
            cur = heapq.heappop(q)
            endpoint = trace[i][2]
            trace[endpoint][1] = cur
            ans[cur] += 1
        elif trace[i][0] == 2:
            cur = trace[i][1]
            heapq.heappush(q, cur)

    print(x)
    print(*ans)