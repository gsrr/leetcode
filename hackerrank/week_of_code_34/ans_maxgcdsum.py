import sys
import pdb

def maximumGcdAndSum(A, B):
    print A
    print B
    max_value = max(max(A), max(B))
    def get(A, max_value):
        okay = [0 for i in range(max_value + 1)]
        for x in A:
            okay[x] = x
        for x in range(1, max_value + 1):
            for y in range(x + x, max_value + 1, x):
                if okay[y]:
                    okay[x] = y
        return okay
    okayA = get(A, max_value)
    okayB = get(B, max_value)
    print okayA
    print okayB
    for i in range(max_value, 0, - 1):
        if okayA[i] > 0 and okayB[i] > 0:
            return(okayA[i] + okayB[i])

if __name__ == "__main__":
    n = int(raw_input().strip())
    A = list(map(int, raw_input().strip().split(' ')))
    B = list(map(int, raw_input().strip().split(' ')))
    #sys.stdin = open('/dev/tty')
    #pdb.set_trace()
    res = maximumGcdAndSum(A, B)
    print(res)
