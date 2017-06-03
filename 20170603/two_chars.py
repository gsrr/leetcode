import collections


def remove_dup(ls):
    find = False
    c = ""
    for i in xrange(1, len(ls)):
        if ls[i] == ls[i - 1]:
            find = True
            c = ls[i]

    if find == True:
        cnt = 0
        for i in xrange(len(ls)):
            if ls[i] == c:
                pass
            else:
                ls[cnt] = ls[i]
                cnt += 1
        del ls[cnt:]
        remove_dup(ls)
    return  
    
def select_char(c1, c2, s):
    ss = []
    for c in s:
        if c == c1 or c == c2:
            ss.append(c)
    return "".join(ss)

def is_two_chars(ss):
    for i in xrange(1, len(ss)):
        if ss[i] == ss[i - 1]:
            return False
    return True

s = "beabeefeab"
ds = collections.Counter(s).most_common()
for i in xrange(len(ds)):
    find = False
    for j in xrange(i + 1, len(ds)):
        ss = select_char(ds[i][0], ds[j][0], s)
        find = is_two_chars(ss)
        if find == True:
            print len(ss)
            break
    if find == True:
        break

#ls = list(s)
#remove_dup(ls)
#print ls

