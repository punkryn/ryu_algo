# # https://www.acmicpc.net/problem/20665
# from sys import stdin
# si = stdin.readline

# if __name__ == '__main__':
#     n, t, p = map(int, si().split())
#     timestamp = [[-1] * (60 * 21 + 1) for _ in range(n + 1)]
#     order = []
#     for _ in range(t):
#         start, end = si().split()
#         if start == end: continue
#         start = int(start[:2]) * 60 + int(start[2:])
#         end = int(end[:2]) * 60 + int(end[2:])
#         order.append((start, end))
#     order.sort(key=lambda x: (x[0], x[1] - x[0]))
    
#     seat = [0] * (n + 1)
#     seat[1] = 1
#     if n >= 2:
#         seat[n] = 2
#     if n >= 3:
#         for num in range(3, n + 1):
#             maxv = -1
#             idx = 3
#             for i in range(2, n):
#                 if seat[i] != 0: continue
#                 l = i
#                 lv = 0
#                 while l - 1 > 1:
#                     l -= 1
#                     if seat[l] == 0:
#                         lv += 1
#                     else:
#                         break
#                 r = i
#                 rv = 0
#                 while r + 1 < n:
#                     r += 1
#                     if seat[r] == 0:
#                         rv += 1
#                     else:
#                         break
                
#                 if maxv < min(lv, rv):
#                     maxv = min(lv, rv)
#                     idx = i
            
#             seat[idx] = num
        
#     seat_conv = [0] * (n + 1)
#     for i in range(1, n + 1):
#         seat_conv[seat[i]] = i
#     seat = seat_conv
    
#     ans = 1260 - 540
#     for i in range(len(order)):
#         s, e = order[i]
#         cnt = 1
#         for j in range(i):
#             s_, e_ = order[j]
#             if s < e_:
#                 cnt += 1
        
#         if seat[cnt] == p:
#             ans -= (e - s)

#     print(ans)
n, guest, p = map(int,input().split())

def to_time(x):
    h, m = divmod(x, 100)
    return 60*h + m - 540

enters = [[] for i in range(721)]
exits = [[] for i in range(721)]
for i in range(guest):
    a, b = map(int,input().split())
    if a == b: continue
    a = to_time(a)
    b = to_time(b)
    enters[a].append((b, i+1))
    exits[b].append(i+1)

seat = [0] * n
def sit():
    L = [-float('inf')] * n
    R = [float('inf')] * n
    if seat[0]: L[0] = 0
    for i in range(1, n):
        L[i] = i if seat[i] else L[i-1]
    if seat[n-1]: R[n-1] = n-1
    for i in range(n-2, -1, -1):
        R[i] = i if seat[i] else R[i+1]
    
    return -max((min(i-L[i], R[i]-i), -i) for i in range(n))[1]

position = {}
ans = 0
for TIME in range(720):
    # exit
    for i in exits[TIME]:
        seat[position[i]] = 0
        del position[i]
    # enter
    enters[TIME].sort()
    for b,i in enters[TIME]:
        j = sit()
        position[i] = j
        seat[j] = i
        print(j, seat)
    ans+= not seat[p-1]
print(ans)