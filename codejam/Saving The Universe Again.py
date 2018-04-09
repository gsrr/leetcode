
import collections

'''
smallese : SSSCC
largest : CCSSS

6
1 CS
2 CS
1 SS
6 SCCSSC 1 + 4 + 4 --> SCSCSC 1 + 2 + 4 --> SCSSCC 1 + 2 + 2 , so answer = 2 
2 CC
3 CSCSS 2 + 4 + 4 --> CSSCS 2 + 2 + 4 --> CSSSC 2 + 2 + 2 --> SCSSC 1 + 2 + 2 --> SSCSC 1 + 1 + 2 --> SSSCC 1 + 1 + 1 , so answer = 5

Case #1: 1
Case #2: 0
Case #3: IMPOSSIBLE
Case #4: 2
Case #5: 0
Case #6: 5

'''

def get_min_dmg(dic):
    return dic['S']

def get_max_dmg(dic):
    base = pow(2, dic['C'])
    return base * dic['S']

def get_dmg(arr):
    base = 1
    dmg = 0
    for i in xrange(len(arr)):
        if arr[i] == "S":
            dmg += base
        elif arr[i] == "C":
            base *= 2
    return dmg

def hack_cnt(shell, prog):
    '''
    simple method
    '''
    dic = collections.Counter(prog)
    min_dmg = get_min_dmg(dic)
    max_dmg = get_max_dmg(dic)
    if shell < min_dmg:
        return "IMPOSSIBLE"

    if shell > max_dmg:
        return "0"

    arr = list(prog)
    cnt = 0
    while get_dmg(arr) > shell:
        cnt += 1
        for i in xrange(len(arr) - 1, 0, -1):
            if arr[i] == "S" and arr[i - 1] == "C":
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                break
    return str(cnt)

def main():
    t = 7
    data = [
        ([1, "CS"], 1),
        ([2, "CS"], 0),
        ([1, "SS"], "IMPOSSIBLE"),
        ([6, "SCCSSC"], 2),
        ([2, "CC"], 0),
        ([3, "CSCSS"], 5),
        ([4, "0"], 0),
    ]
    for i in xrange(t):
        print "Case #%d:%s"%(i, hack_cnt(*data[i][0]))

if __name__ == "__main__":
    main()
