# https://www.acmicpc.net/problem/2573
import sys
si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m = map(int, si().split())
    MAP = [list(map(int, si().split())) for _ in range(n)]

    iceberg_cnt = 0
    flag = True
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if MAP[i][j] > 0:
                iceberg_cnt += 1
                if flag:
                    start_point = (i, j)
                flag = False
                
    stack = []
    removed = []
    sign = 1
    ans = 0
    while True:
        sign *= -1
        count = 0
        ans += 1

        stack.append(start_point)
        MAP[start_point[0]][start_point[1]] *= -1
        while stack:
            x, y = stack.pop()
            count += 1
            
            ocean_cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if MAP[nx][ny] == 0:
                    ocean_cnt += 1
                elif MAP[nx][ny] * -1 * sign > 0:
                    stack.append((nx, ny))
                    MAP[nx][ny] *= -1
            
            if MAP[x][y] * sign - ocean_cnt <= 0:
                removed.append((x, y))
            else:
                MAP[x][y] -= ocean_cnt * sign
                start_point = (x, y)
        
        if count != iceberg_cnt:
            print(ans - 1)
            break

        while removed:
            x, y = removed.pop()
            MAP[x][y] = 0
            iceberg_cnt -= 1
        
        if iceberg_cnt == 0:
            print(0)
            break