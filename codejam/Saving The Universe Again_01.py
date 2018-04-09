
import collections

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
    t = int(raw_input())
    for i in xrange(t):
        shell, prog = raw_input().split()
        print "Case #%d: %s"%(i + 1, hack_cnt(int(shell), prog))

if __name__ == "__main__":
    main()
