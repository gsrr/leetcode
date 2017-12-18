def ans(s):
    minn = len(s) 
    arr = [0] * 26
    pos = [0] * 26
    for i in xrange(len(s)):
        c = ord(s[i]) - ord('a')
        arr[c] += 1
        pos[c] = i

    for i in xrange(len(arr)):
        if arr[i] == 1 and pos[i] < minn:
            minn = pos[i]
    if minn == len(s):
        return -1
    else:
        return minn
s = "leetcode"
print ans(s)

s = "loveleetcode"
print ans(s)

print sorted(s)

