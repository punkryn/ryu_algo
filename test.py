import sys
si = sys.stdin.readline

def main():
    n, m = map(int, si().split())
    arr = sorted(list(map(int, si().split())))
    s = [0] * 10
    visited = [0] * n
    def go(depth, cur):
        if depth == m + 1:
            for i in range(1, m + 1):
                print(s[i], end=' ')
            print()
            return
        
        prev = 0
        for i in range(n):
            if visited[i] == 1 or prev == arr[i]:
                continue
            
            prev = arr[i]
            visited[i] = 1
            s[depth] = arr[i]
            go(depth + 1, prev)
            s[depth] = 0
            visited[i] = 0
        
    go(1, 0)

if __name__ == '__main__':
    main()