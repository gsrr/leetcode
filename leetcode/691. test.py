import itertools

def combinations_1(ts):
    # list all combinations
    cnt = 0
    mts = [(1, "a"), (2, "b"), (4, "c"), (8, "d"), (16, "e")]
    for i in xrange(1 << len(ts)):
        elem = []
        for v, k in mts:
            if i & v != 0:
                elem.append(k)
        if len(elem) == 0:
            print "()"
        else:
            print elem
        cnt += 1
    print cnt

def combinations_2(ts):
    cnt = 0
    for i in xrange(len(ts) + 1):
        it = itertools.combinations(ts, i)
        for elem in it:
            print elem
            cnt += 1
    print cnt

def lib_comb(ts, k, ret):
    if k == 0:
        print ret

    for i in xrange(len(ts)):
        ret.append(ts[i])
        lib_comb(ts[i + 1:], k - 1, ret)
        ret.pop()

def combinations_3(ts):
    for i in xrange(len(ts) + 1):
        ret = []
        lib_comb(ts, i, ret)

from collections import Counter

def dic_test():
    a = {"a" : 1}
    b = {"a" : 1, "b" : 2}
    # print a & b, exception

    ca = Counter(a)
    cb = Counter(b)
    print ca & cb

def main():
    ts = "abcde"
    #combinations_3(ts)
    dic_test()

if __name__ == "__main__":
    main()

