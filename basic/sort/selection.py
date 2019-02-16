import main

def ans1(arr):
    arr.sort()
    return ",".join([ str(x) for x in arr])


def selection(arr, j):
    lmin = j
    for i in xrange(j + 1, len(arr)):
        if arr[i] < arr[lmin]:
            lmin = i
    return lmin
    

def ans(arr):
    for i in xrange(len(arr)):
        j = selection(arr, i)
        arr[i], arr[j] = arr[j], arr[i]
    return ",".join([ str(x) for x in arr])

if __name__ == "__main__":
    main.main(ans)
