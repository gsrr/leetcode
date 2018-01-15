

def ans(arr, st, e):
    if st >= e:
        return 

    pval = arr[st]
    i = st + 1
    j = e - 1
    while True:
        while i < e and arr[i] < pval:
            i += 1
        
        while j > st and arr[j] >= pval:
            j -= 1

        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[st] = arr[st], arr[j]
    ans(arr, st, j)
    ans(arr, j + 1, e)

def ans2(arr, st, e):
    '''
    Lomuto Partitioning
    '''
    if st >= e:
        return 

    pval = arr[st]
    j = st + 1
    for i in xrange(j, e):
        if arr[i] <= pval:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j - 1], arr[st] = arr[st], arr[j - 1]
    ans2(arr, st, j - 1)
    ans2(arr, j, e)

def ans3(arr):
    '''
    partition array
    '''
    if len(arr) <= 1:
        return arr

    pval = arr[0]
    smaller = [x for x in arr[1:] if x < pval]
    bigger = [x for x in arr[1:] if x >= pval]
    return ans3(smaller) + [pval] + ans3(bigger)

class Solution:
    def quickSort(self, arr):
        #ans(arr, 0, len(arr))
        #ans2(arr, 0, len(arr))
        print ans3(arr)

def main():
    sol = Solution()
    with open("input", "r") as fr:
        num = map(int, fr.readline().strip())[0]
        for i in xrange(num):
            arr = map(int, fr.readline().strip().split())
            sol.quickSort(arr)
            print " ".join(map(str, arr))


if __name__ == "__main__":
    main()
