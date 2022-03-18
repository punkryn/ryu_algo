# https://www.acmicpc.net/problem/2877
import sys
si = sys.stdin.readline

def main():
    k = int(si())
    a = [2]
    sum_ = 2
    while sum_ < k:
        sum_ += a[-1] * 2
        a.append(a[-1] * 2)

    ans = []
    s, e = sum_ - a[-1] + 1, sum_
    for i in range(len(a) - 1, -1, -1):
        if s <= k <= e - a[i] // 2:
            ans.append('4')
            e = e - a[i] // 2
        elif e - a[i] // 2 + 1 <= k <= sum_:
            ans.append('7')
            s = e - a[i] // 2 + 1
    print(int(''.join(ans)))

if __name__ == '__main__':
    main()