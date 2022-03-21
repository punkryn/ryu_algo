# https://www.acmicpc.net/problem/17615
import sys
si = sys.stdin.readline
INF = int(1e9)
def main():
    n = int(si())
    balls = list(si().strip())

    red = 0
    for ball in balls:
        if ball == 'R':
            red += 1
    blue = n - red
    
    ans = min(red, blue)
    cnt = 0
    for i in range(n):
        if balls[i] != balls[0]: break
        cnt += 1
    
    if balls[0] == 'R':
        ans = min(ans, red - cnt)
    else:
        ans = min(ans, blue - cnt)
    
    cnt = 0
    for i in range(n - 1, -1, -1):
        if balls[i] != balls[n - 1]: break
        cnt += 1
    
    if balls[n - 1] == 'R':
        ans = min(ans, red - cnt)
    else:
        ans = min(ans, blue - cnt)
    
    print(ans)

if __name__ == '__main__':
    main()