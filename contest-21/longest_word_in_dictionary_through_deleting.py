
def find(base, s, r):
    start = 0
    tmp_start = 0
    for i in xrange(len(s)):
        if start == len(base):
            return r
        for j in xrange(start, len(base)):
            if s[i] == base[j]:
                tmp_start = j + 1
                break
        if tmp_start == start:
            return r
        else:
            start = tmp_start
    if r < s:
        return r
    return s

def ans(s, d):
    ret = ""
    for i in d:
        ret = find(s, d[i], ret)
    return ret

s = "abpcplea"
d = ["ale","apple","monkey","plea"]
print ans(s, d)
