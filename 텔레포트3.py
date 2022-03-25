# https://www.acmicpc.net/problem/12908
import sys
si = sys.stdin.readline

def go(depth, cur, cnt):
    if depth == 3:
        # ans = min(ans, abs(cur[0] - xe) + abs(cur[1] - ye))
        print(cur)
        return

    go(depth + 1, cur, cnt)
    cur.append(tel[depth])
    go(depth + 1, cur, cnt + 1)
    cur.pop()

def oper(depth, total, cur, arr):
    if depth == len(arr):
        ans = min(ans, total + abs(cur[0] - xe) + abs(cur[1] - ye))
        return
    
    calc = abs(cur[0] - arr[depth][0]) + abs(cur[1] - arr[depth][1])
    oper(depth + 1, total + calc + 10, (arr[depth][2], arr[depth][3]), arr)
    calc = abs(cur[0] - arr[depth][2]) + abs(cur[1] - arr[depth][3])
    oper(depth + 1, total + calc + 10, (arr[depth][0], arr[depth][1]), arr)

if __name__ == '__main__':
    xs, ys = map(int, si().split())
    xe, ye = map(int, si().split())
    tel = [list(map(int, si().split())) for _ in range(3)]

    ans = int(1e15)
    go(0, [], 0)