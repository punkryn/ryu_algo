# https://www.acmicpc.net/problem/2473
# -97 -6 -2 6 98
import sys
si = sys.stdin.readline

def main():
    n = int(si())
    props = sorted(list(map(int, si().split())))
    if n == 3:
        print(*sorted(props))
    else:
        # print(props)
        ans = float("inf")
        r = []
        for l in range(n-2):
            target = props.pop()
            l_, r_ = 0, len(props) - 1
            while l_ < r_:
                total = target + props[l_] + props[r_]
                if abs(total) < ans:
                    ans = abs(total)
                    r = [target, props[l_], props[r_]]

                if total < ans:
                    l_ += 1
                else:
                    r_ -= 1

                if ans == 0:
                    break

            if ans == 0:
                break

        print(*sorted(r))

if __name__ == "__main__":
    main()