

def recur_util(path, dic, chars, idx):
    if len(chars) == idx:
        cand = "".join(path)
        if dic.has_key(cand) == False:
            return (False, cand)
        return (True, "-")

    
    for i in xrange(len(chars[idx])):
        path.append(chars[idx][i])
        ret, cand = recur_util(path, dic, chars, idx + 1)
        if ret == False:
            return (False, cand)
        path.pop()
    return (True, cand)

def a_whold_new_word(n, length, arr):
    #print n, length, arr
    dic = {}
    for i in xrange(len(arr)):
        dic[arr[i]] = True

    chars = []
    for i in xrange(length):
        cdic = {}
        for j in xrange(n):
            cdic[arr[j][i]] = True
        chars.append(list(cdic.keys()))
    
    #print chars
    idx = 0
    path = []
    for i in xrange(len(chars[idx])):
        path.append(chars[idx][i])
        ret, cand = recur_util(path, dic, chars, idx + 1)
        if ret == False:
            return (False, cand)
        path.pop()
    return (True, "-")

def main():
    t = int(raw_input())
    for i in xrange(t):
        n, length = list(map(int, raw_input().split()))
        arr = []
        for j in xrange(n):
            arr.append(raw_input().strip())
        print "Case #%d: %s"%(i+1, a_whold_new_word(n, length, arr)[1])

if __name__ == "__main__":
    main()
