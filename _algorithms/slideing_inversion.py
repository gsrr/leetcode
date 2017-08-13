import copy
def getSum2(BITree, index, max_val):
    s = 0
    t = max_val
    while t > index:
        s += BITree[t]
        t -= t & (-t)

    while index > t:
        s -= BITree[index]
        index -= index & (-index)
    return s

def getSum(BITree, index):
    s = 0
    t = index
    while t > 0:
        s += BITree[t]
        t -= t & (-t)
    return s

def updateBIT(BITree, max_val, index, val):
    while index <= max_val:
        BITree[index] += val
        index += index & (-index)

def convert_arr(arr):
    arr2 = list(arr)
    arr.sort()
    dic = {}
    cnt = 1
    val = arr[0]
    dic[val] = cnt
    for i in xrange(1, len(arr)):
        if arr[i] != val:
            cnt += 1
            val = arr[i]
            dic[val] = cnt
    arr3 = []
    for i in xrange(len(arr2)):
        arr3.append(dic[arr2[i]])
    return arr3

def main():
    n,m = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    carr = convert_arr(arr)
    BIT = [0] * (n + 3)
    cnt = 0
    for i in xrange(m - 1, -1, -1):
        cnt += getSum(BIT, carr[i] - 1)
        updateBIT(BIT, n + 2, carr[i], 1)
    ans = cnt
    for i in xrange(m, len(carr)):
        dcnt = getSum(BIT, carr[i - m] - 1)
        cnt -= dcnt
        updateBIT(BIT, n + 2, carr[i - m], -1)
        acnt = getSum2(BIT, carr[i], n + 2)
        updateBIT(BIT, n + 2, carr[i], 1)
        cnt += acnt
        ans += cnt
    print ans


if __name__ == "__main__":
    main()
