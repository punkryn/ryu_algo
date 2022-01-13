import sys
si = sys.stdin.readline

def main():
    n = int(si())
    props = sorted(list(map(int, si().split())))

    maximum = float('inf')
    cand = []
    for i in range(n - 2):
        target = props.pop()
        l, r = 0, len(props) - 1
        while l < r:
            total = target + props[l] + props[r]
            if abs(total) < maximum:
                maximum = abs(total)
                cand = [target, props[l], props[r]]
            
            if total < maximum:
                l += 1
            else:
                r -= 1
            
            if maximum == 0:
                break
        if maximum == 0:
            break
    
    print(*sorted(cand))

if __name__ == "__main__":
    main()