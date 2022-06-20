# https://www.acmicpc.net/problem/1493
import sys
si = sys.stdin.readline


if __name__ == '__main__':
    length, width, height = map(int, si().split())
    n = int(si())
    cube = sorted([list(map(int, si().split())) for _ in range(n)], reverse=True)

    total = length * width * height

    ans = prev = 0
    for i, cnt in cube:
        cur_len = 1 << i
        prev <<= 3

        cur_cnt = (length // cur_len) * (width // cur_len) * (height // cur_len) - prev
        cur_cnt = min(cnt, cur_cnt)
        ans += cur_cnt
        prev += cur_cnt
    
    if total == prev:
        print(ans)
    else:
        print(-1)