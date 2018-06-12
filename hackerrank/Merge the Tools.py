def ans(ss):
    ret = []
    hist = set([])
    for i in xrange(len(ss)):
        if ss[i] in hist:
            continue
        ret.append(ss[i])
        hist.add(ss[i])
    return "".join(ret)

def merge_the_tools(s, k):
    # your code goes here
    i = 0
    while i < len(s):
        print ans(s[i: i + k])
        i += k

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
