import operator

def ans1(txt):
    arr = []
    for i in xrange(len(txt)):
        arr.append([txt[i:], i])
    
    arr.sort()
    return [ x[1] for x in arr]


def print_arr(suffixes):
    for s in suffixes:
        print s.index, s.rank
    print

class suffix:
    def __init__(self):
        self.index = 0
        self.rank = [0, 0]

def compare(a, b):
    if a.rank[0] == b.rank[0]:
        ret = -1 if a.rank[1] < b.rank[1] else 1
    else:
        ret = -1 if a.rank[0] < b.rank[0] else 1
    return ret

def myrange(start, end, step):
    while start <= end:
        yield start
        start *= step

def ans2_nlogn(txt):
    
    # compare the first two character first
    #
    suffixes = [suffix() for _ in xrange(len(txt))]
    for i in xrange(len(suffixes)):
        suffixes[i].index = i
        suffixes[i].rank[0] = ord(txt[i]) - ord('a')
        suffixes[i].rank[1] = ord(txt[i + 1]) - ord('a') if i + 1 < len(suffixes) else -1
    suffixes.sort(compare)
    pre_index = [0] * len(suffixes)

    # compare the first 4 character --> 8 character -> ...
    #
    for k in myrange(4, 2 * len(txt), 2):
        pre_rank = list(suffixes[0].rank)
        suffixes[0].rank[0] = 0
        pre_index[suffixes[0].index] = suffixes[0].rank[0]

        for i in xrange(1, len(suffixes)):
            if pre_rank == suffixes[i].rank:
                pre_rank = list(suffixes[i].rank)
                suffixes[i].rank[0] = suffixes[i - 1].rank[0]
            else:
                pre_rank = list(suffixes[i].rank)
                suffixes[i].rank[0] = suffixes[i - 1].rank[0] + 1
            pre_index[suffixes[i].index] = suffixes[i].rank[0]

        for i in xrange(len(suffixes)):
            next_index = suffixes[i].index + (k/2)
            if next_index >= len(suffixes):
                suffixes[i].rank[1] = -1
            else:
                suffixes[i].rank[1] = pre_index[next_index]
        suffixes.sort(compare)
    return [ x.index for x in suffixes ]

def ans3_nlogn(txt):
    suffixes = [suffix() for _ in xrange(len(txt))]
    for i in xrange(len(suffixes)):
        suffixes[i].index = i
        suffixes[i].rank[0] = ord(txt[i]) - ord('a')
        suffixes[i].rank[1] = ord(txt[i + 1]) - ord('a') if i + 1 < len(suffixes) else -1
    suffixes.sort(compare)

    for k in myrange(4, 2 * len(txt), 2):
        # rank1 update
        pre_rank = list(suffixes[0].rank)
        suffixes[0].rank[0] = 0
        for i in xrange(1, len(suffixes)):
            crank = list(suffixes[i].rank)
            suffixes[i].rank[0] = suffixes[i - 1].rank[0]
            if pre_rank != crank:
                suffixes[i].rank[0] += 1
            pre_rank = crank

        index_rank1 = [0] * len(suffixes)
        for i in xrange(len(suffixes)):
            index_rank1[suffixes[i].index]= suffixes[i].rank[0]

        for i in xrange(len(suffixes)):
            next_index = suffixes[i].index + (k/2)
            if next_index >= len(suffixes):
                suffixes[i].rank[1] = -1
            else:
                suffixes[i].rank[1] = index_rank1[next_index]
        suffixes.sort(compare)
    return [ x.index for x in suffixes ]

def buildSuffixArray(txt):
    #return ans1(txt)
    print "ans2:", ans2_nlogn(txt)
    print "ans3:", ans3_nlogn(txt)

def main():
    txt = "banana"
    suffix_array = buildSuffixArray(txt);
    print txt
    print suffix_array

main()
