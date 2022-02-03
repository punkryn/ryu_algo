# def solution(n, k, cmd):
#     answer = ''
    
#     table = ['O'] * n
#     deleted = []
    
#     for c in cmd:
#         if len(c) == 3:
#             op, num = c.split()
#             if op == 'D':
#                 cnt = 0
#                 while cnt < int(num):
#                     print(cnt, num)
#                     if table[k+1] == 'X':
#                         k += 1
#                         continue
#                     else:
#                         k += 1
#                         cnt += 1
#             elif op == 'U':
#                 cnt = 0
#                 while cnt < int(num):
#                     print(cnt, num)
#                     if table[k-1] == 'X':
#                         k -= 1
#                         continue
#                     else:
#                         k -= 1
#                         cnt += 1
#         else:
#             if c == 'C':
#                 print(k)
#                 if k == n - 1:
#                     table[k] = 'X'
#                     deleted.append(k)
#                     for i in range(k-1, -1, -1):
#                         if table[i] == 'O':
#                             k = i
#                             break
#                 else:
#                     for i in range(k + 1, n):
#                         if table[i] == 'O':
#                             deleted.append(k)
#                             table[k] = 'X'
#                             k = i
#                             break
#                     else:
#                         deleted.append(k)
#                         table[k] = 'X'
#                         for i in range(k-1, -1, -1):
#                             if table[i] == 'O':
#                                 k = i
#                                 break
                    
#             elif c == 'Z':
#                 rev = deleted.pop()
#                 table[rev] = 'O'
    
#     answer = ''.join(table)
    # return answer

def solution(n, k, cmd):
    answer = ''
    
    node = {}
    node[0] = [None, 1]
    node[n-1] = [n-2, None]
    for i in range(1, n-1):
        node[i] = [i-1, i+1]
    deleted = []
    check = [0] * n
    for c in cmd:
        if len(c) == 3:
            op, num = c.split()
            if op == 'D':
                for _ in range(int(num)):
                    k = node[k][1]
            elif op == 'U':
                for _ in range(int(num)):
                    k = node[k][0]
        else:
            op = c
            if op == 'C':
                if not node[k][1]:
                    deleted.append(k)
                    check[k] = 1
                    k = node[k][0]
                    node[k][1] = None
                else:
                    if k != 0:
                        deleted.append(k)
                        check[k] = 1
                        node[node[k][0]][1] = node[k][1]
                        node[node[k][1]][0] = node[k][0]
                        k = node[k][1]
                    else:
                        deleted.append(k)
                        check[k] = 1
                        node[node[k][1]][0] = None
                        k = node[k][1]
            elif op == 'Z':
                rev = deleted.pop()
                check[rev] = 0
                for i in range(rev - 1, -1, -1):
                    if check[i] == 0:
                        node[i][1] = rev
                        node[rev][0] = i
                        break
                else:
                    node[rev][0] = None
                
                for i in range(rev + 1, n):
                    if check[i] == 0:
                        node[i][0] = rev
                        node[rev][1] = i
                        break
                else:
                    node[rev][1] = None
    
    ans = ['X'] * n
    ans[k] = 'O'
    tmp = k
    while True:
        print(tmp)
        if not node[tmp][0]:
            ans[tmp] = 'O'
            break
        ans[node[tmp][0]] = 'O'
        tmp = node[tmp][0]

    print(node)
    tmp = k
    while True:
        # print(tmp)
        if not node[tmp][1]:
            ans[tmp] = 'O'
            break
        ans[node[tmp][1]] = 'O'
        tmp = node[tmp][1]
    print(node)
    answer = ''.join(ans)
    return answer

n, k = 8, 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
solution(n, k, cmd)
