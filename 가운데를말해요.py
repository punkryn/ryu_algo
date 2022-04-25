# https://www.acmicpc.net/problem/1655
import sys
import heapq
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    maxq = []
    minq = []
    ans = []
    for i in range(n):
        tmp = int(si())
        if i == 0:
            heapq.heappush(maxq, -tmp)
            ans.append(tmp)
        elif i == 1:
            if tmp > -maxq[0]:
                heapq.heappush(minq, tmp)
                ans.append(-maxq[0])
            else:
                heapq.heappush(minq, -heapq.heappop(maxq))
                heapq.heappush(maxq, -tmp)
                ans.append(tmp)
        else:
            if tmp > minq[0]:
                heapq.heappush(minq, tmp)
            else:
                heapq.heappush(maxq, -tmp)
            
            if len(maxq) + 1 < len(minq):
                heapq.heappush(maxq, -heapq.heappop(minq))
            elif len(minq) + 1 < len(maxq):
                heapq.heappush(minq, -heapq.heappop(maxq))
            
            if (len(minq) + len(maxq)) % 2 == 1:
                if len(minq) > len(maxq):
                    ans.append(minq[0])
                elif len(maxq) > len(minq):
                    ans.append(-maxq[0])
            else:
                ans.append(-maxq[0])
    
    for a in ans:
        print(a)