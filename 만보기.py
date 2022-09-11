# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1284&sca=9040
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
  x, y = mis()
  ans = 0
  for i in range(3, 18):
    for j in range(10):
      s = [str(j)] * i
      for k in range(10):
        if j == k: continue
        for l in range(i):
          tmp = s[l]
          s[l] = str(k)
          
          if s[0] != '0' and x <= int(''.join(s)) <= y:
            ans += 1

          s[l] = tmp
  print(ans)