import heapq
hq = []
heapq.heappush(hq, (1, 3))
heapq.heappush(hq, (1, 3))
heapq.heappush(hq, (1, 3))
heapq.heappush(hq, (1, 3))
heapq.heappush(hq, (1, 3))
heapq.heappush(hq, (1, 2))
heapq.heappush(hq, (1, 6))
heapq.heappush(hq, (1, 5))
heapq.heappush(hq, (1, 4))
print(heapq.heappop(hq))
