# https://www.acmicpc.net/problem/15558
import sys
from collections import deque
si = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, si().split())
    l = si().strip()
    r = si().strip()

    lines = [l, r]

    q = deque()
    q.append((0, 1, 0))
    visited = set()
    visited.add((0, 1))
    ans = 0
    while q:
        cur_line, cur_pos, cur_time = q.popleft()

        if cur_pos + 1 > n:
            ans = 1
            break
        if lines[cur_line][cur_pos] == '1' and (cur_line, cur_pos + 1) not in visited:
            q.append((cur_line, cur_pos + 1, cur_time + 1))
            visited.add((cur_line, cur_pos + 1))
        
        if cur_pos - 1 > 0 and cur_pos - 1 > cur_time + 1 and lines[cur_line][cur_pos - 2] == '1' and (cur_line, cur_pos - 2) not in visited:
            q.append((cur_line, cur_pos - 1, cur_time + 1))
            visited.add((cur_line, cur_pos - 1))
        
        if cur_pos + k > n:
            ans = 1
            break

        nxt_line = (cur_line + 1) % 2
        if lines[nxt_line][cur_pos + k - 1] == '1' and (nxt_line, cur_pos + k - 1) not in visited:
            q.append((nxt_line, cur_pos + k, cur_time + 1))
            visited.add((nxt_line, cur_pos + k))
    print(ans)