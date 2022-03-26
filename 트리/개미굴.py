# https://www.acmicpc.net/problem/14725
import sys
si = sys.stdin.readline

class Trie:
    def __init__(self):
        self.children = {}
    
    def insert(self, infos):
        cur = self.children
        
        for info in infos:
            if info not in cur:
                cur[info] = {}
            cur = cur[info]
        cur[0] = True
    
    def traverse(self, cur, level):
        if 0 in cur:
            return
        
        for key in sorted(cur):
            print('--' * level + key)
            self.traverse(cur[key], level + 1)

if __name__ == '__main__':
    n = int(si())
    nest = Trie()
    for _ in range(n):
        nest.insert(si().split()[1:])
    nest.traverse(nest.children, 0)