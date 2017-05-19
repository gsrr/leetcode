
dic = {
    '0' : '1',
    '1' : '0',
}

def generate(s):
    ret = []
    for i in xrange(len(s)):
        ret.append(dic[s[i]])
    return s + "".join(ret)


s = "0"
while len(s) < 1000:
    print s
    s = generate(s)
print s
