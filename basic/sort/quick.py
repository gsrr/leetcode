import main

def quick1(arr):
    '''
    Hoare partition
    '''
    if len(arr) == 0:
        return []

    if len(arr) == 1:
        return [arr[0]]

    pval = arr[0]
    i = 1
    j = len(arr) - 1
    while i <= j:
        while i < len(arr) and arr[i] < pval:
            i += 1
        while j > -1 and arr[j] > pval:
            j -= 1
        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    arr[0], arr[j] = arr[j], arr[0]
    larr = quick1(arr[0:j])
    rarr = quick1(arr[j + 1:])
    return larr + [arr[j]] + rarr

def quick2(arr, s, e):
    if s >= e:
        return
    pval = arr[s]
    i = s + 1
    j = e
    while i <= j:
        while i < len(arr) and arr[i] < pval:
            i += 1
        while j > -1 and arr[j] > pval:
            j -= 1
        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    arr[s], arr[j] = arr[j], arr[s]
    quick2(arr, j + 1, e)
    quick2(arr, s, j - 1)
        
def quick3(arr, s, e):
    '''
    Lomuto Partitioning
    '''
    if s >= e:
        return
    pval = arr[s]
    j = s + 1
    for i in xrange(s + 1, e + 1):
        if arr[i] <= pval:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    
    j = j - 1
    arr[s], arr[j] = arr[j], arr[s]
    quick2(arr, j + 1, e)
    quick2(arr, s, j - 1)
    
def ans(arr):
    #arr = quick1(arr)
    #quick2(arr, 0, len(arr) - 1)
    quick3(arr, 0, len(arr) - 1)
    return ",".join( [str(x) for x in arr] )

if __name__ == "__main__":
    main.main(ans)
