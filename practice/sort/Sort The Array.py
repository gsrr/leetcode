#code

def quickSort(arr, s, e):
    if s >= e:
        return
    
    # partition
    pval = arr[s]
    i = s + 1
    for j in range(s + 1, e):
        if arr[j] < pval:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[s], arr[i - 1] = arr[i - 1], arr[s]
    
    quickSort(arr, s, i - 1)
    quickSort(arr, i, e)

def main():
    n = int(input())
    for i in range(n):
        m = int(input())
        arr = map(int, input().split())
        arr = list(arr)
        quickSort(arr, 0, len(arr))
        print(" ".join(list(map(str, arr))))
        
if __name__ == "__main__":
    main()
