import operator

def ans1(txt):
    arr = []
    for i in xrange(len(txt)):
        arr.append([txt[i:], i])
    
    arr.sort()
    return [ x[1] for x in arr]

def buildSuffixArray(txt):
    return ans1(txt)

def main():
    txt = "banana"
    suffix_array = buildSuffixArray(txt);
    print txt
    print suffix_array

main()
