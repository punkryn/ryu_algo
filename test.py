from sys import setrecursionlimit
setrecursionlimit(int(1e9))
class Trie:
    def __init__(self):
        self.finish = False
        self.cnt = 0
        self.node = dict()
    
    def insert(self, word, idx):
        if len(word) == idx:
            self.finish = True
            return
        
        if word[idx] not in self.node:
            self.node[word[idx]] = Trie()
        self.node[word[idx]].cnt += 1
        self.node[word[idx]].insert(word, idx + 1)
    
    def Print(self, cur):
        for nxt in cur.node:
            print(nxt, cur.node[nxt].cnt, cur.node[nxt].finish)
            self.Print(cur.node[nxt])
    
    def traverse(self, cur, prev):
        ret = 0
        for nxt in cur.node:
            if cur.node[nxt].cnt >= 2:
                ret += cur.node[nxt].cnt
            elif prev >= 2 and cur.node[nxt].cnt == 1:
                ret += 1
            elif prev == 0:
                ret += 1
            ret += self.traverse(cur.node[nxt], cur.node[nxt].cnt)
        return ret

def solution(words):
    answer = 0
    

    node = Trie()
    for word in words:
        node.insert(word, 0)

    node.Print(node)
        
    answer = node.traverse(node, 0)
    
    return answer

words = ['go', 'gone', 'guild']
print(solution(words))