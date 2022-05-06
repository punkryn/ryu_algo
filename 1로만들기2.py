# https://www.acmicpc.net/problem/12852
import sys
from collections import deque
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    
    q = deque([n])
    visited = {n: 0}
    while q:
        cur = q.popleft()
        if cur == 1:
            break

        nxt = cur // 3
        if cur % 3 == 0 and nxt not in visited:
            visited[nxt] = cur
            q.append(nxt)
        
        nxt = cur // 2
        if cur % 2 == 0 and nxt not in visited:
            visited[nxt] = cur
            q.append(nxt)
        
        nxt = cur - 1
        if nxt not in visited:
            visited[nxt] = cur
            q.append(nxt)
                        
    s = 1
    ans = [s]
    while visited[s] > 0:
        ans.append(visited[s])
        s = visited[s]
    print(*ans[::-1])