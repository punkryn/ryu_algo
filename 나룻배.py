# https://www.acmicpc.net/problem/2065
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    m, t, n = mis()
    
    l, r = [], []
    for _ in range(n):
        time, pos = si().split()
        if pos == 'left':
            l.append((int(time), _))
        else:
            r.append((int(time), _))
    
    l, r = deque(sorted(l)), deque(sorted(r))
    
    curTime = 0
    curPos = 0

    toRight = []
    toLeft = []
    ans = [0] * n
    while (l or r) or (toRight or toLeft):
        if not curPos:
            for time, idx in toLeft:
                ans[idx] = curTime
            toLeft = []

            while l and l[0][0] <= curTime and len(toRight) < m:
                toRight.append(l.popleft())
            
            if not toRight:
                if l and r:
                    if l[0][0] <= r[0][0]:
                        curTime = l[0][0]
                    else:
                        curTime = curTime + t if r[0][0] <= curTime else r[0][0] + t
                        curPos = 1
                elif l:
                    curTime = l[0][0]
                elif r:
                    curTime = curTime + t if r[0][0] <= curTime else r[0][0] + t
                    curPos = 1
                    
                continue
            curPos = 1

        else:
            for time, idx in toRight:
                ans[idx] = curTime
            toRight = []

            while r and r[0][0] <= curTime and len(toLeft) < m:
                toLeft.append(r.popleft())
            
            if not toLeft:
                if l and r:
                    if r[0][0] <= l[0][0]:
                        curTime = r[0][0]
                    else:
                        curTime = curTime + t if l[0][0] <= curTime else l[0][0] + t
                        curPos = 0
                elif r:
                    curTime = r[0][0]
                elif l:
                    curTime = curTime + t if l[0][0] <= curTime else l[0][0] + t
                    curPos = 0
                
                continue
            curPos = 0
        
        curTime += t

    for v in ans:
        print(v)