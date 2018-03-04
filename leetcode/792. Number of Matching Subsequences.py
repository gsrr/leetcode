import collections


def isSubsequence(s, t):
    queue = collections.deque(s)
    for c in t:
        if not queue: return True
        if c == queue[0]:
            queue.popleft()
    return not queue

def ans1(S, words):
    cnt = 0
    for w in words:
        if isSubsequence(w, S):
            cnt += 1
    return cnt
    
def ans2(S, words):
    dic = collections.defaultdict(list)
    for i in xrange(len(S)):
        dic[S[i]].append(i)
    cnt = 0
    for w in words:
        widx = -1
        find = True
        for c in w:
            if dic.has_key(c) == False:
                find = False
                break
            find_idx = False
            for idx in dic[c]:
                if idx > widx:
                    find_idx = True
                    widx = idx
                    break
            if find_idx == False:
                find = False
                break
            
        if find:
            cnt += 1    
    return cnt
 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
print ans2(S, words)
