import sys
input = sys.stdin.readline
def solution(ballon):
    answer = []
    idx = 0
    checked = [0] * n
    while True:
        checked[idx] = 1
        answer.append(idx + 1)
        if sum(checked) == n:
            break
        move = ballon[idx]
        while move != 0:
            if move > 0:
                idx = (idx + 1) % n
                if checked[idx] == 0:
                    move -= 1
            else:
                idx = (idx - 1) % n
                if checked[idx] == 0:
                    move += 1
        checked[idx] = 1
            
        # idx = (idx + ballon[idx]) % n
        # if checked[idx] == 1:
        #     if move > 0:
        #         while checked[idx] == 1:
        #             idx = (idx + 1) % n
        #     else:
        #         while checked[idx] == 1:
        #             idx = (n + idx - 1) % n
    return answer
n = int(input())
ballon = list(map(int, input().split()))
print(' '.join(map(str, solution(ballon))))