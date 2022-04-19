# https://www.acmicpc.net/problem/17276
from re import M
import sys
import copy
si = sys.stdin.readline

def clockwise(matrix, n):
    mid = n // 2
    mat = copy.deepcopy(matrix)
    for i in range(n):
        for j in range(n):
            if not (i == j or j == mid or i == mid or i + j == n - 1):
                continue
            if i < mid and j < mid:
                mat[i][mid] = matrix[i][j]
            elif j == mid and i < mid:
                mat[i][n - 1 - i] = matrix[i][j]
            elif i < mid and j > mid:
                mat[mid][j] = matrix[i][j]
            elif i == mid and j > mid:
                mat[j][j] = matrix[i][j]
            elif i > mid and j > mid:
                mat[i][mid] = matrix[i][j]
            elif i > mid and j == mid:
                mat[i][n - i - 1] = matrix[i][j]
            elif i > mid and j < mid:
                mat[mid][j] = matrix[i][j]
            elif i == mid and j < mid:
                mat[j][j] = matrix[i][j]

    return mat

def counterclockwise(matrix, n):
    mid = n // 2
    mat = copy.deepcopy(matrix)
    for i in range(n):
        for j in range(n):
            if not (i == j or j == mid or i == mid or i + j == n - 1):
                continue
            if i == j:
                mat[mid][j] = matrix[i][j]
            elif j == mid:
                mat[i][i] = matrix[i][j]
            elif i + j == n - 1:
                mat[i][mid] = matrix[i][j]
            elif i == mid:
                mat[n - j - 1][j] = matrix[i][j]
    return mat

def Print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print()

def main():
    n, d = map(int, si().split())
    matrix = [list(map(int, si().split())) for _ in range(n)]
    
    if d > 0:
        for _ in range(d // 45):
            matrix = clockwise(matrix, n)
        Print(matrix)
    else:
        for _ in range(-d // 45):
            matrix = counterclockwise(matrix, n)
        Print(matrix)

if __name__ == "__main__":
    for _ in range(int(si())):
        main()