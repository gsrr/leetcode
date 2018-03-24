#code

def ans(arr):
    arr2 = arr * 2
    #print (arr2)
    gsum = arr2[0]
    tsum = arr2[0]
    path = 1
    for i in range(1, len(arr2)):
        if path == len(arr):
            tsum -= arr2[i - len(arr)]
            path -= 1
            j = i - len(arr) + 1
            ttsum = tsum
            tpath = path
            while j < i:
                ttsum -= arr2[j]
                tpath -= 1
                if ttsum > tsum:
                    tsum = ttsum
                    path = tpath
                j += 1
        if tsum < 0:
        #if tsum < 0:
            tsum = 0
            path = 0
        tsum += arr2[i]
        path += 1
        gsum = max(gsum, tsum)
    return gsum

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print (ans(arr))#code

def ans(arr):
    arr2 = arr * 2
    #print (arr2)
    gsum = arr2[0]
    tsum = arr2[0]
    path = 1
    for i in range(1, len(arr2)):
        if path == len(arr):
            tsum -= arr2[i - len(arr)]
            path -= 1
            j = i - len(arr) + 1
            ttsum = tsum
            tpath = path
            while j < i:
                ttsum -= arr2[j]
                tpath -= 1
                if ttsum > tsum:
                    tsum = ttsum
                    path = tpath
                j += 1
        if tsum < 0:
        #if tsum < 0:
            tsum = 0
            path = 0
        tsum += arr2[i]
        path += 1
        gsum = max(gsum, tsum)
    return gsum

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print (ans(arr))
