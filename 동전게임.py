# https://www.acmicpc.net/problem/9079
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    for _ in range(int(si())):
        board = [si().split() for _ in range(3)]
        
        st = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'H':
                    st |= 1 << i * 3 + j
        print(st)