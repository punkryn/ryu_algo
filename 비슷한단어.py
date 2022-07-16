# https://www.acmicpc.net/problem/2179
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())
    words_ = [si().strip() for _ in range(n)]
    words = sorted([[words_[i], i] for i in range(n)])
    ans = 0
    length = [0] * n
    for i in range(len(words) - 1):
        if words[i][0] == words[i + 1][0]: continue
        cnt = 0
        for j in range(min(len(words[i][0]), len(words[i + 1][0]))):
            if words[i][0][j] != words[i + 1][0][j]:
                break
            cnt += 1
        ans = max(ans, cnt)
        length[words[i][1]] = max(length[words[i][1]], cnt)
        length[words[i + 1][1]] = max(length[words[i + 1][1]], cnt)
    flag = True
    prev = ''
    for i in range(n):
        if flag:
            if length[i] == ans:
                flag = False
                print(words_[i])
                prev = words_[i][:ans]
        else:
            if length[i] == ans and words_[i][:ans] == prev:
                print(words_[i])
                break