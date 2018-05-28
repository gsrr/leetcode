
def findTheAbsentStudents(n, arr):
    ret = set(range(1, n + 1))
    for i in xrange(len(arr)):
        if arr[i] in ret:
            ret.remove(arr[i])
    ret = list(ret)
    ret.sort()
    return [ str(x) for x in ret ]


n = 10
arr = [1, 2, 2, 3, 4, 5, 2, 8, 9, 10]
print findTheAbsentStudents(n, arr)
