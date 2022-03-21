# https://www.acmicpc.net/problem/17615
import sys
si = sys.stdin.readline
def main():
    n = int(si())
    balls = list(si().strip())

    red = balls.count('R')
    blue = n - red
    ans = min(red, blue)

    cnt = 0
    for i in range(n):
        if balls[0] != balls[i]:
            break
        cnt += 1
    
    if balls[0] == 'R':
        ans = min(ans, red - cnt)
    else:
        ans = min(ans, blue - cnt)
    
    cnt = 0
    for i in range(n - 1, -1, -1):
        if balls[-1] != balls[i]:
            break
        cnt += 1
    
    if balls[-1] == 'R':
        ans = min(ans, red - cnt)
    else:
        ans = min(ans, blue - cnt)
    
    print(ans)

if __name__ == '__main__':
    main()