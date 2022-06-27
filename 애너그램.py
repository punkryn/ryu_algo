# https://www.acmicpc.net/problem/6443
import sys
from itertools import permutations
si = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

# class Trie:
#     def __init__(self):
#         self.children = dict()
#         self.flag = False
    
#     def insert(self, word, idx):
#         if len(word) == idx:
#             self.flag = True
#             return
        
#         if word[idx] not in self.children:
#             self.children[word[idx]] = Trie()
#         self.children[word[idx]].insert(word, idx + 1)
    
#     def traverse(self, cur=[]):
#         if self.flag:
#             print(''.join(cur))
#         for key in sorted(self.children):
#             cur.append(key)
#             self.children[key].traverse(cur)
#             cur.pop()

def go(depth, cur):
    if depth == len(word):
        if cur not in used:
            used.add(cur)
            print(cur)
        return
    
    for i in range(26):
        if alpha[i] > 0:
            alpha[i] -= 1
            go(depth + 1, cur + chr(i + ord('a')))
            alpha[i] += 1

if __name__ == '__main__':
    n = int(si())

    for i in range(n):
        word = sorted(si().strip())
        used = set()
        alpha = [0] * 26
        for w in word:
            alpha[ord(w) - ord('a')] += 1
        go(0, '')
    
    # for word in words:
    #     trie = Trie()
    #     for per in permutations(word, len(word)):
    #         trie.insert(per, 0)
    #     trie.traverse()