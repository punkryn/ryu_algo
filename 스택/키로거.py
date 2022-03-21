# https://www.acmicpc.net/problem/5397
# 1
# -d>a<<<<<a>>>>>b<pq<<<z--
# aapqb
import sys
si = sys.stdin.readline

class Node:
    def __init__(self, data, prev = None, nxt = None):
        self.prev = prev
        self.nxt = nxt
        self.data = data
    
    def insert(self, prev, nxt):
        self.prev = prev
        self.nxt = nxt
        prev.nxt = self
        nxt.prev = self
    
    def delete(self):
        self.prev.nxt = self.nxt
        self.nxt.prev = self.prev


def main():
    string = si().strip()
    head = Node('head')
    tail = Node('tail')
    head.nxt = tail
    tail.prev = head
    cursor = head
    for s in string:
        if s == '<':
            if cursor.prev and cursor.prev.prev:
                cursor = cursor.prev
            elif cursor.prev and not cursor.prev.prev:
                cursor = head
        elif s == '>':
            if cursor.nxt and cursor.nxt.nxt:
                cursor = cursor.nxt
        elif s == '-':
            if cursor.data == 'head':
                continue
            else:
                cursor.delete()
                # if not cursor.nxt.nxt:
                cursor = cursor.prev
                # else:
                #     cursor = cursor.nxt
        else:
            tmp = Node(s, cursor, cursor.nxt)
            tmp.insert(cursor, cursor.nxt)
            cursor = tmp
    
    cur = head
    while cur.nxt.nxt:
        print(cur.nxt.data, end='')
        cur = cur.nxt
    print()

if __name__ == '__main__':
    for _ in range(int(si())):
        main()