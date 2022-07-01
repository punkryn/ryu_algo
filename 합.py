# https://www.acmicpc.net/problem/1132
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n = int(si())
    words = []
    for i in range(10):
        words.append([0, chr(ord('A') + i)])
    
    not0 = [False] * 10
    for _ in range(n):
        word = si().strip()
        for i in range(len(word)):
            if i == 0:
                not0[ord(word[i]) - ord('A')] = True
            words[ord(word[i]) - ord('A')][0] += 10 ** (len(word) - 1 - i)
    
    words.sort(reverse=True)

    if words[9][0] != 0:
        for i in range(9, -1, -1):
            if not not0[ord(words[i][1]) - ord('A')]:
                tmp = words[i]
                words.remove(tmp)
                words.append(tmp)
                break
    
    ans = 0
    for i in range(10):
        ans += words[i][0] * (9 - i)
    print(ans)