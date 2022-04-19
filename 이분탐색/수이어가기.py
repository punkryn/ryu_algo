# https://www.acmicpc.net/problem/2635
import sys
si = sys.stdin.readline

def deter(mid):
    t = [n, mid]
    idx = 0
    while True:
        nxt = t[idx] - t[idx + 1]
        if nxt < 0:
            break
        t.append(nxt)
        idx += 1
    return t

if __name__ == '__main__':
    n = int(si())
    
    ans = 0
    ans_list = []
    for i in range(n // 2, n + 1):
        tmp = deter(i)
        if ans < len(tmp):
            ans = len(tmp)
            ans_list = tmp
    print(ans)
    print(*ans_list)