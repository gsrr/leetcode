#code

class node:
    def __init__(self, ch):
        self.val = ch
        self.next = [None] * 26
        self.isEnd = False

def trie_insert(root, word):
    tmp = root
    for c in word:
        idx = ord(c) - ord('a')
        if tmp.next[idx] == None:
            new = node(c)
            tmp.next[idx] = new
        tmp = tmp.next[idx]
    tmp.isEnd = True

def recur_util(node, path):
    if node == None:
        return
    
    path.append(node.val)
    if node.isEnd == True:
        print ("".join(path))
        
    for i in range(len(node.next)):
        recur_util(node.next[i], path)
    path.pop()

def traverse(root):
    path = []
    for i in range(len(root.next)):
        recur_util(root.next[i], path)

def trie_search(root, tgt):
    tmp = root
    for c in tgt:
        idx = ord(c) - ord('a')
        if tmp.next[idx] == None:
            return 0
        else:
            tmp = tmp.next[idx]
            if tmp.isEnd == True:
                return 1
    return 0

def recur_util2(node, tgt, level):
    pass

def trie_search_recur(node, tgt, level):
    if node == None:
        return 0
    
    if node.isEnd == True:
        return 1
    
    if level == len(tgt):
        return 0
        
    idx = ord(tgt[level]) - ord('a')
    return trie_search_recur(node.next[idx], tgt, level + 1)
    
def ans(words, tgt):
    root = node("")
    for w in words:
        trie_insert(root, w)
    #traverse(root)
    #return trie_search(root, tgt)
    return trie_search_recur(root, tgt, 0)
    
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(input().strip().split())
    tgt = input().strip()
    print (ans(arr, tgt))
