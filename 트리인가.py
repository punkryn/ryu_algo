# https://www.acmicpc.net/problem/6416
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    number = 1
    indegree = dict()
    while True:
        line = si().strip()
        if line == '-1 -1': break
        elif line == '': continue

        end = False
        arr = list(map(int, line.split()))
        flag = False
        for i in range(0, len(arr), 2):
            if arr[i] == 0 and arr[i + 1] == 0:
                flag = True
                break
            
            if arr[i] not in indegree:
                indegree[arr[i]] = 0
            if arr[i + 1] not in indegree:
                indegree[arr[i + 1]] = 0

            indegree[arr[i + 1]] += 1
        
        if flag:
            if not indegree:
                print(f'Case {number} is a tree.')
                number += 1
                indegree = dict()
                continue

            root_cnt = 0
            flag = False
            for key in indegree:
                if indegree[key] == 0:
                    root_cnt += 1
                
                if indegree[key] > 1:
                    flag = True
                    break
            
            if flag:
                print(f'Case {number} is not a tree.')
                number += 1
                indegree = dict()
                continue

            if root_cnt == 0 or root_cnt > 1:
                print(f'Case {number} is not a tree.')
                number += 1
                indegree = dict()
                continue

            print(f'Case {number} is a tree.')
            
            number += 1
            indegree = dict()