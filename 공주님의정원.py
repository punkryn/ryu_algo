# https://www.acmicpc.net/problem/2457
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if __name__ == '__main__':
    n = int(si())

    for i in range(1, 13):
        day[i] += day[i - 1]

    d = []
    for _ in range(n):
        ms, ds, me, de = mis()
        d.append((day[ms - 1] + ds, day[me - 1] + de))

    d.sort(key=lambda x: (x[0], -x[1]))

    s, e = day[2] + 1, day[11] + 1

    ans = 0
    cnt = idx = 0
    while s < e:
        flag = False

        for i in range(idx, n):
            if d[i][0] > s:
                break

            if cnt < d[i][1]:
                flag = True
                cnt = d[i][1]
                idx = i + 1
        
        if flag:
            s = cnt
            ans += 1
        else:
            break
        
    print(ans if cnt >= e else 0)