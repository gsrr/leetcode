import main

def ans1(arr):
    arr.sort()
    return ",".join([ str(x) for x in arr])

def insertion(arr, index):
    val = arr[index]
    j = index - 1
    while j > - 1 and arr[j] > val:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = val

def ans(arr):
    for i in xrange(len(arr)):
        insertion(arr, i)
    return ",".join([ str(x) for x in arr])

if __name__ == "__main__":
    main.main(ans)
