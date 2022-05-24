# # https://www.acmicpc.net/problem/1644
# import sys
# si = sys.stdin.readline

# if __name__ == '__main__':
#     n = int(si())
#     s = [2]
#     for i in range(3, n + 1, 2):
#         flag = False
#         for num in s:
#             if num * num > i:
#                 break
#             if i % num == 0:
#                 flag = True
#                 break
#         if not flag:
#             s.append(i)

#     cur = 0
#     r = 0
#     ans = 0
#     for l in range(len(s)):
#         while r < len(s) and cur < n:
#             cur += s[r]
#             r += 1
        
#         if cur == n:
#             ans += 1
        
#         cur -= s[l]
#     print(ans)
def prime(n):
    if n < 2: return []
    n += 1
    save = [1] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if save[i // 2]: 
            save[i * i // 2::i] = [0] * ((n - i * i - 1) // (2 * i) + 1)
        print(save)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if save[i]]

N = int(input())
arr = [0] + prime(N)
print(arr)
for i in range(1, len(arr)): arr[i] += arr[i - 1]
a, b = 0, 1
ans = 0

while a < b < len(arr):
    s = arr[b] - arr[a]
    if s <= N:
        if s == N: ans += 1
        b += 1
    else: a += 1

print(ans)
