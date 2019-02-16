import main

def mergeall(arr1, arr2):
    ret = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            ret.append(arr1[i])
            i += 1
        else:
            ret.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        ret.append(arr1[i])
        i += 1

    while j < len(arr2):
        ret.append(arr2[j])
        j += 1
    return ret

def merge1(arr):
    if len(arr) == 0:
        return []

    if len(arr) == 1:
        return [arr[0]]

    mid = len(arr) // 2
    larr = merge1(arr[:mid])
    rarr = merge1(arr[mid:])
    return mergeall(larr, rarr)

def mergeall2(arr, s, mid, e):
    i = s
    j = mid + 1
    while i <= mid and j <= e:
        if arr[i] <= arr[j]:
            i += 1
        else:
            val = arr[j]
            for k in xrange(j, i, -1):
                arr[k] = arr[k - 1]
            arr[i] = val
            i += 1
            j += 1
            mid += 1

def merge2(arr, s, e):
    if s >= e:
        return

    mid = (s + e) // 2
    merge2(arr, s, mid)
    merge2(arr, mid + 1, e)
    mergeall2(arr, s, mid, e)

def ans(arr):
    #arr = merge1(arr)
    merge2(arr, 0, len(arr) - 1)
    return ",".join( [str(x) for x in arr] )

if __name__ == "__main__":
    main.main(ans)
