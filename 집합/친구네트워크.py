import sys
si = sys.stdin.readline
DEBUG = False

def find_parent(parent, node):
    if parent.get(node, node) != node:
        return find_parent(parent, parent.get(node, node))
    return node

def main():
    f = int(si())
    a = []
    name = {}
    len_dict = {}
    for _ in range(f):
        n1, n2 = si().split()
        p1 = find_parent(name, n1)
        p2 = find_parent(name, n2)
        if p1 not in len_dict:
            len_dict[p1] = 1
        if p2 not in len_dict:
            len_dict[p2] = 1
        if p1 == p2:
            print(len_dict[p1])
        elif len_dict[p1] > len_dict[p2]:
            len_dict[p1] += len_dict[p2]
            name[p2] = p1
            print(len_dict[p1])
        else:
            len_dict[p2] += len_dict[p1]
            name[p1] = p2
            print(len_dict[p2])

        # if n1 not in name and n2 not in name:
        #     name[n1] = len(a)
        #     name[n2] = len(a)
        #     tmp = set()
        #     tmp.add(n1)
        #     tmp.add(n2)
        #     a.append(tmp)
        #     print(2)
        # else:
        #     if n2 not in name:
        #         name[n2] = name[n1]
        #         a[name[n1]].add(n2)
        #         print(len(a[name[n1]]))
        #     elif n1 not in name:
        #         name[n1] = name[n2]
        #         a[name[n2]].add(n1)
        #         print(len(a[name[n2]]))
        #     else:
        #         idx1 = name[n1]
        #         idx2 = name[n2]
        #         if idx1 > idx2:
        #             idx1, idx2 = idx2, idx1
        #         if idx1 == idx2:
        #             print(len(a[idx1]))
        #             continue
        #         for n in a[idx2]:
        #             name[n] = idx1
        #         a[idx1] = a[idx1].union(a[idx2])
        #         print(len(a[idx1]))
        
        if DEBUG:
            print(a)
            print(name)
    
if __name__ == '__main__':
    for _ in range(int(si())):
        main()