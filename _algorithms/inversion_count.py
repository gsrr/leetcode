
def getSum(RBITree, BITree, index):
    s = 0
    t = index
    while t > 0:
        s += BITree[t]
        if BITree[t] > 0:
            RBITree[t] += 1
        t -= t & (-t)
    return s

def updateBIT(BITree, max_val, index, val):
    while index <= max_val:
        BITree[index] += val
        index += index & (-index)

def updateRBIT(RBITree, max_val, index, val):
    while index > 0:
        RBITree[index] += val
        index -= index & (-index)
    
def getSumRBIT(RBITree, max_val, index):
    s = 0
    t = index
    while t <= max_val:
        s += RBITree[t]
        t += t & (-t)
    return s

def getInvCount(arr):
    cnt = 0
    max_val = max(arr)
    BIT = [0] * (max_val + 1)
    RBIT = [0] * (max_val + 1)
    for i in xrange(len(arr) - 1, -1, -1):
        cnt += getSum(RBIT, BIT, arr[i] - 1)
        print "getSum", arr[i], BIT, cnt
        updateBIT(BIT, max_val, arr[i], 1);
        print "update", arr[i], BIT

    print RBIT
    print getSumRBIT(RBIT, max_val, 2)
    updateRBIT(RBIT, max_val, 2 - 1, -1);
    print RBIT
    print getSumRBIT(RBIT, max_val, 1)
    updateBIT(BIT, max_val, 2, -1);
    print "update", arr[i], BIT
    return cnt

def main():
    arr = [9, 8, 7, 7, 4, 2, 1]
    print getInvCount(arr)


if __name__ == "__main__":
    main()
