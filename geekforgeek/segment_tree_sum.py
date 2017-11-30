
import math

def constructSTUtil(arr, ss, se, st, si):
    if ss == se:
        st[si] = arr[ss]
    else:
        mid = (ss + se) / 2
        st[si] = constructSTUtil(arr, ss, mid, st, si * 2 + 1) + constructSTUtil(arr, mid + 1, se, st, si * 2 + 2)
    return st[si]

def constructST(arr):
    h = int(math.ceil(math.log(len(arr), 2)))
    st = [0] * (pow(2, h + 1) - 1)
    constructSTUtil(arr, 0, len(arr) - 1, st, 0)
    return st

def getSumUtil(st, ss, se, si , q):
    qs = q[0]
    qe = q[1]
    if qe < ss or qs > se:
        return 0

    if qs <= ss and qe >= se:
        return st[si]

    mid = (ss + se) / 2
    return getSumUtil(st, ss, mid, si * 2 + 1, q) + getSumUtil(st, mid + 1, se, si * 2 + 2, q)

def getSum(st, n, q):
    return getSumUtil(st, 0, n - 1, 0, q)


arr = [1, 3, 5, 7, 9, 11]
st = constructST(arr)
print st
query = [(1, 3), (3, 5)]
for q in query:
    print q, getSum(st, len(arr), q)
