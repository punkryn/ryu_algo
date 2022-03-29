# https://www.acmicpc.net/problem/21942
import sys
si = sys.stdin.readline

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def time_convert():
    return month[(MM - 1)] * 24 * 60 + (dd - 1) * 24 * 60 + hh * 60 + mm

if __name__ == '__main__':
    n, l, f = si().split()
    n = int(n)
    f = int(f)

    fs = l.split('/')
    fss = fs[1].split(':')
    lending_period = int(fs[0]) * 60 * 24 + int(fss[0]) * 60 + int(fss[1])
    
    for i in range(1, 13):
        month[i] += month[i - 1]

    ans = dict()
    members = dict()
    for _ in range(n):
        info = si().split()
        yyyy, MM, dd = map(int, info[0].split('-'))
        hh, mm = map(int, info[1].split(':'))
        parts = info[2]
        name = info[3]

        minutes = time_convert()
        
        # 이름x => 대여
        if name not in members:
            members[name] = dict()
            members[name][parts] = minutes
        else:
            # 이름o 부품o => 반납
            if parts in members[name]:
                diff = minutes - members[name][parts]
                if diff > lending_period:
                    if name not in ans:
                        ans[name] = (diff - lending_period) * f
                    else:
                        ans[name] += (diff - lending_period) * f
                members[name].pop(parts)
            else:
                # 이름o 부품x => 대여
                members[name][parts] = minutes
        # print(members)
        # print(ans)
    
    if not ans:
        print(-1)

    for key in sorted(ans):
        print(key, ans[key])