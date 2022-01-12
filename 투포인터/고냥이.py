# https://www.acmicpc.net/problem/16472
import sys
si = sys.stdin.readline
n = int(si())
string = si().strip()

alpha = [0] * 30
alpha_cnt = 0

def add(w):
    global alpha_cnt
    alpha[ord(w) - ord('a')] += 1
    if alpha[ord(w) - ord('a')] == 1:
        alpha_cnt += 1

def erase(w):
    global alpha_cnt
    alpha[ord(w) - ord('a')] -= 1
    if alpha[ord(w) - ord('a')] == 0:
        alpha_cnt -= 1

l, ans = 0, 0
for r in range(len(string)):
    add(string[r])
    while alpha_cnt > n:
        erase(string[l])
        l += 1
    ans = max(ans, r - l + 1)

# def deter(w):
#     global alpha_cnt
#     if alpha[ord(w) - ord('a')] != 0:
#         # alpha[ord(w) - ord('a')] += 1
#         return True
#     else:
#         if alpha_cnt < n:
#             alpha_cnt += 1
#             return True
#         return False

# r, ans = -1, 0
# for l in range(len(string)):
#     while r + 1 < len(string) and deter(string[r + 1]):
#         r += 1
#         alpha[ord(string[r]) - ord('a')] += 1
    
#     alpha[ord(string[l]) - ord('a')] -= 1
#     if alpha[ord(string[l]) - ord('a')] == 0:
#         alpha_cnt -= 1
#     # print(l, r, alpha)
#     ans = max(ans, r - l + 1)

print(ans)