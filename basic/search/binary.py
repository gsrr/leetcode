import main
import time


def binsearch1(arr, val):
    s = 0
    e = len(arr) - 1
    mid = ( s + e ) // 2
    while arr[mid][0] != val:
        mval = arr[mid][0]
        if val > mval:
            s = mid + 1
        else:
            e = mid - 1
        mid = (s + e) // 2 
    return str(arr[mid][1])

def binsearch2(arr, val):
    s = 0
    e = len(arr) - 1
    while s <= e:
        mid = (s + e) // 2
        mval = arr[mid][0]
        if mval == val:
            return str(arr[mid][1])
        elif val > mval:
            s = mid + 1
        else:
            e = mid - 1

def binsearch_recur(arr, val, s, e):
    mid = (s + e) // 2
    if val == arr[mid][0]:
        return str(arr[mid][1])

    if val > arr[mid][0]:
        return binsearch_recur(arr, val, mid + 1, e)
    else:
        return binsearch_recur(arr, val, s, mid - 1)

def binsearch_left(arr, val):
    s = 0
    e = len(arr) - 1
    while s <= e:
        mid = (s + e) // 2
        mval = arr[mid][0]
        if val > mval: ###
            s = mid + 1
        else:
            e = mid - 1
    return str(arr[e + 1][1])

def binsearch_right(arr, val):
    s = 0
    e = len(arr) - 1
    while s <= e:
        mid = (s + e) // 2
        mval = arr[mid][0]
        if val >= mval: ###
            s = mid + 1
        else:
            e = mid - 1
    return str(arr[s - 1][1])

def ans(arr, val):
    narr = []
    for i in xrange(len(arr)):
        narr.append([arr[i], i])
    narr.sort()
    return binsearch_recur(narr, val, 0, len(narr) - 1)

if __name__ == "__main__":
    main.main(ans)
