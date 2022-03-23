# https://www.acmicpc.net/problem/2204
import sys
si = sys.stdin.readline

def main():
    while True:
        n = int(si())
        if n == 0:
            return
        words = [si().strip() for _ in range(n)]
        words.sort(key=lambda x: x.lower())
        print(words[0])

if __name__ == '__main__':
    main()