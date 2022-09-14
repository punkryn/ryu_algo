# https://www.acmicpc.net/problem/17281
import sys
from itertools import permutations
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def hit(state, k, q):
    cnt = 0
    for i in range(3, -1, -1):
        if state[i] == -1: continue
        if i + k > 3:
            q[state[i]] = 1
            state[i] = -1
            cnt += 1
        else:
            state[i + k] = state[i]
            state[i] = -1
    return cnt

def calc(order):
    point = 0
    idx = 0
    for i in range(n):
        flag = [1] * 9
        state = [-1] * 4
        outCount = 0
        while outCount < 3:
            while True:
                if flag[order[idx]]:
                    break

                idx = (idx + 1) % 9

            cur = order[idx]
            flag[order[idx]] = 0

            state[0] = cur
                

            if 1 <= r[i][cur] <= 4:
                point += hit(state, r[i][cur], flag)
            else:
                outCount += 1
                # q.append(cur)
                flag[order[idx]] = 1

            idx = (idx + 1) % 9
        
    return point



if __name__ == '__main__':
    n = int(si())
    r = [list(mis()) for _ in range(n)]
    
    ans = 0
    for per in permutations(range(1, 9), 8):
        ans = max(ans, calc(list(per[:3]) + [0] + list(per[3:])))

    print(ans)

