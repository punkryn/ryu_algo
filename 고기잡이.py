# https://www.acmicpc.net/problem/7573
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n, l, m = mis()
    coord = sorted([list(mis()) for _ in range(m)], key=lambda x: (x[0], x[1]))
    
    cand = [(i, l // 2 - i) for i in range(1, l // 2)]
    
    ans = 0
    for a, b in cand:
        r = 0
        for l in range(m):
            while r < m and coord[r][0] - coord[l][0] <= a:
                r += 1
            
            cur = sorted(coord[l: r], key=lambda x: x[1])

            r_ = 0
            for l_ in range(len(cur)):
                while r_ < len(cur) and cur[r_][1] - cur[l_][1] <= b:
                    r_ += 1
                
                ans = max(ans, r_ - l_)
    print(ans)
                    

    # for x, y in coord:
    #     for x_, y_ in coord:
    #         for cx, cy in cand:
    #             cnt = 0
    #             for x__, y__ in coord:
    #                 if x <= x__ <= x + cx and y_ <= y__ <= y_ + cy:
    #                     cnt += 1
    #             ans = max(ans, cnt)
    # print(ans)
