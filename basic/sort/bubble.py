import main

def ans1(arr):
    arr.sort()
    return ",".join([ str(x) for x in arr])

def bubble_max(arr, j):
    for i in xrange(len(arr) - 1 - j):
        if arr[i + 1] < arr[i]:
            arr[i + 1], arr[i] = arr[i], arr[i + 1]

def bubble_min(arr, j):
    for i in xrange(len(arr) - 1, j, -1):
        if arr[i - 1] > arr[i]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]


def ans(arr):
    for i in xrange(len(arr)):
        #bubble_max(arr, i)
        bubble_min(arr, i)
    return ",".join([ str(x) for x in arr])

if __name__ == "__main__":
    main.main(ans)
