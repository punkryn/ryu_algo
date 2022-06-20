# https://www.acmicpc.net/problem/14728
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, t = map(int, si().split())
    a = [list(map(int, si().split())) for _ in range(n)]
    cand = {0: 0}
    ans = 0
    for k, s in a:
        tmp_dict = dict()
        for key in cand:
            tmp = key + k
            nxt_score = cand[key] + s
            if tmp > t: continue
            tmp_dict[tmp] = nxt_score
        
        for key in tmp_dict:
            if key in cand:
                if cand[key] < tmp_dict[key]:
                    cand[key] = tmp_dict[key]
            else:
                cand[key] = tmp_dict[key]

            ans = max(ans, cand[key])
    print(ans)