# https://www.acmicpc.net/problem/12908
import sys
si = sys.stdin.readline

def go(depth, cur, cnt):
    if depth == 3:
        oper(0, 0, (xs, ys), cur)
        return

    go(depth + 1, cur, cnt)
    cur.append(tel[depth])
    go(depth + 1, cur, cnt + 1)
    cur.pop()

def oper(depth, total, cur, arr):
    global ans
    if depth == len(arr):
        ans = min(ans, total + abs(cur[0] - xe) + abs(cur[1] - ye))
        return
    
    for i in range(len(arr)):
        if visited[i] != 0: continue

        visited[i] = 1
        calc = abs(cur[0] - arr[i][0]) + abs(cur[1] - arr[i][1])
        oper(depth + 1, total + calc + 10, (arr[i][2], arr[i][3]), arr)
        calc = abs(cur[0] - arr[i][2]) + abs(cur[1] - arr[i][3])
        oper(depth + 1, total + calc + 10, (arr[i][0], arr[i][1]), arr)
        visited[i] = 0

if __name__ == '__main__':
    xs, ys = map(int, si().split())
    xe, ye = map(int, si().split())
    tel = [list(map(int, si().split())) for _ in range(3)]
    visited = [0] * 3
    ans = int(1e15)
    go(0, [], 0)
    print(ans)