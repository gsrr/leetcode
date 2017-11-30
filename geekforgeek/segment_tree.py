import math

def constructSTUtil(arr, ss, se, st, si):
    if ss == se:
        st[si] = arr[ss]
        return st[si]
        
    mid = (ss + se) / 2
    st[si] = constructSTUtil(arr, ss, mid, st, si * 2 + 1) + constructSTUtil(arr, mid + 1, se, st, si * 2 + 2)
    
    return st[si]

def constructST(arr):
    height = int(math.ceil(math.log(len(arr),2)))
    st = [0] * (pow(2, height + 1) - 1)
    constructSTUtil(arr, 0, len(arr) - 1, st, 0)
    return st

def getSumUtil(st, ss, se, qs, qe, si):
    if (qs > se or qe < ss):
        return 0

    if (qs <= ss and qe >= se):
        return st[si]

    mid = (ss + se) / 2
    return getSumUtil(st, ss, mid, qs, qe, 2 * si + 1) + getSumUtil(st, mid + 1, se, qs, qe, 2 * si + 2)

def getSum(st, n, q):
    return getSumUtil(st, 0, n - 1, q[0], q[1], 0)

def ans_1(arr, query):
    st = constructST(arr)
    print st
    for q in query:
        print q, getSum(st, len(arr), q)



'''
(1, 3) --> 15
'''
def main():
    arr = [1, 3, 5, 7, 9, 11]
    query = [(1, 3), (3, 5)]
    print ans_1(arr, query)

if __name__ == "__main__":
    main()
