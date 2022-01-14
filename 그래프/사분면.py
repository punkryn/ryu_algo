# https://www.acmicpc.net/problem/1891
import sys
si = sys.stdin.readline

def main():
    d, num = si().strip().split()
    x, y = map(int, si().split())
    d = int(d)

    def make_pos(num):
        start = 1
        end = 2 ** len(num)
        for i in range(len(num)):
            if num[i] in ['1', '4']:
                start = (start + end) // 2 + 1
            else:
                end = (start + end) // 2
        return start
    
    def make_y_pos():
        start = 1
        end = 2 ** len(num)
        for i in range(len(num)):
            if num[i] in ['3', '4']:
                start = (start + end) // 2 + 1
            else:
                end = (start + end) // 2
        return start
    
    x_pos = make_pos(num)
    y_pos = make_y_pos()
    if 1 <= x_pos + x <= 2 ** d and 1 <= y_pos - y <= 2 ** d:
        mx = x_pos + x
        my = y_pos - y
        start = 1
        end = 2 ** d
        ans = ''
        tmp = []
        for _ in range(len(num)):
            mid = (start + end) // 2
            if start <= mx <= mid:
                tmp.append([2, 3])
                end = mid
            else:
                tmp.append([1, 4])
                start = mid + 1
        
        start = 1
        end = 2 ** d
        for t_ in tmp:
            mid = (start + end) // 2
            if start <= my <= mid:
                ans += str(t_[0])
                end = mid
            else:
                ans += str(t_[1])
                start = mid + 1

        print(ans)
    else:
        print(-1)

if __name__ == '__main__':
    main()