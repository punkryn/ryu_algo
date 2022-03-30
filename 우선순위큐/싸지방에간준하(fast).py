# https://www.acmicpc.net/problem/12764
import sys
import heapq
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    orders = [list(map(int, si().split())) for _ in range(n)]
    orders.sort()
    q = []
    ans = []
    cnt = 0
    answer = []
    for i in range(n):
        s, e = orders[i]
        while q and q[0][0] < s:
            cur = heapq.heappop(q)
            end, idx = cur
            heapq.heappush(ans, idx)
        
        if not ans:
            answer.append(1)
            heapq.heappush(q, (e, cnt))
            cnt += 1
        else:
            number = heapq.heappop(ans)
            heapq.heappush(q, (e, number))
            answer[number] += 1
    
    print(len(answer))
    print(*answer)