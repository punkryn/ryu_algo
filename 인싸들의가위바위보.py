# https://www.acmicpc.net/problem/16986
import sys
si = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def go(c1, c2, g_idx, m_idx, cnt, win, g_win, m_win):
    global ans
    if ans == 1:
        return

    if win == k:
        ans = 1
        return

    if g_win == k or m_win == k:
        return
    
    if cnt == n:
        return

    if (c1 == 0 and c2 == 1) or (c1 == 1 and c2 == 0):
        if g_idx == 20:
            return
        for i in range(n):
            if visited[i]: continue
            visited[i] = True
            if matrix[i][gyeong[g_idx] - 1] == 2:
                go(0, 2, g_idx + 1, m_idx, cnt + 1, win + 1, g_win, m_win)
            else:
                go(1, 2, g_idx + 1, m_idx, cnt + 1, win, g_win + 1, m_win)
            visited[i] = False
    elif (c1 == 0 and c2 == 2) or (c1 == 2 and c2 == 0):
        if m_idx == 20:
            return
        for i in range(n):
            if visited[i]: continue
            visited[i] = True
            if matrix[i][minho[m_idx] - 1] == 2:
                go(0, 1, g_idx, m_idx + 1, cnt + 1, win + 1, g_win, m_win)
            else:
                go(1, 2, g_idx, m_idx + 1, cnt + 1, win, g_win, m_win + 1)
            visited[i] = False
    elif (c1 == 1 and c2 == 2) or (c1 == 2 and c2 == 1):
        if g_idx == 20 or m_idx == 20:
            return
        if matrix[gyeong[g_idx] - 1][minho[m_idx] - 1] == 2:
            go(0, 1, g_idx + 1, m_idx + 1, cnt, win, g_win + 1, m_win)
        else:
            go(0, 2, g_idx + 1, m_idx + 1, cnt, win, g_win, m_win + 1)

if __name__ == '__main__':
    n, k = map(int, si().split())
    matrix = [list(map(int, si().split())) for _ in range(n)]
    gyeong = list(map(int, si().split()))
    minho = list(map(int, si().split()))
    
    visited = [False] * n
    ans = 0
    go(0, 1, 0, 0, 0, 0, 0, 0)
    print(ans)