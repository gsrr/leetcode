import main

def heapify(arr, n, i):
    lc = (2 * i) + 1
    rc = (2 * i) + 2
    p = i
    if lc < n and arr[lc] < arr[p]:
        p = lc

    if rc < n and arr[rc] < arr[p]:
        p = rc

    if p == i:
        return

    arr[p], arr[i] = arr[i], arr[p]
    heapify(arr, n, p)

def heapify_iter(arr, n, i):
    p = i
    while p < n:
        np = p
        lc = (2 * p) + 1
        rc = (2 * p) + 2
        if lc < n and arr[lc] < arr[np]:
            np = lc

        if rc < n and arr[rc] < arr[np]:
            np = rc

        if p == np:
            break

        arr[p], arr[np] = arr[np], arr[p]
        p = np

def heapify_all(arr):
    for i in xrange(len(arr) - 1, -1, -1):
        #heapify(arr, len(arr), i)
        heapify_iter(arr, len(arr), i)

def heap(arr):
    heapify_all(arr)
    for i in xrange(len(arr)):
        e = len(arr) - 1 - i
        arr[0], arr[e] = arr[e], arr[0]
        heapify(arr, len(arr) - 1 - i, 0 )
            
    return arr[::-1]

        

def ans(arr):
    arr = heap(arr)
    return ",".join( [str(x) for x in arr] )

if __name__ == "__main__":
    main.main(ans)
