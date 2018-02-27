#code
def ans1(arr, k):
    for i in range(len(arr)):
        index = arr[i] % k
        arr[index] += k
    #print (arr)
    midx = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[midx]:
            if int(arr[i]/k) == int(arr[midx]/k):
                continue
            midx = i
    return midx

t = int(input())
for i in range(t):  
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    #print (n, k, arr)
    print (ans1(arr, k))
