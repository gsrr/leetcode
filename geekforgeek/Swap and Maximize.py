#code
def ans3(arr):
    arr.sort()
    i = 1
    j = len(arr) - 1
    summ = 0
    cnt = 1
    while cnt < len(arr):
        if cnt % 2 == 0:
            summ += abs(arr[i] - arr[j + 1])
            i += 1
        else:
            summ += abs(arr[j] - arr[i - 1])
            j -= 1
        cnt += 1
    
    if cnt % 2 == 0:
        summ += abs(arr[0] - arr[i])
    else:
        summ += abs(arr[0] - arr[j])
    return summ

def ans2(arr):
    arr.sort()
    i = 1
    j = len(arr) - 1
    summ = 0
    narr = [arr[0]]
    cnt = 1
    while cnt < len(arr):
        if cnt % 2 == 0:
            narr.append(arr[i])
            i += 1
        else:
            narr.append(arr[j])
            j -= 1
        summ += abs(narr[-1] - narr[-2])
        cnt += 1
    summ += abs(narr[0] - narr[-1])    
    return summ

def ans1(arr):
    arr.sort()
    i = 0
    j = len(arr) - 1
    summ = 0
    narr = []
    cnt = 0
    while cnt < len(arr):
        if cnt % 2 == 0:
            narr.append(arr[i])
            i += 1
        else:
            narr.append(arr[j])
            j -= 1
        cnt += 1
    #print (narr)
    for i in range(1, len(narr) + 1):
        summ += abs(narr[i % len(narr)] - narr[i - 1])
    return summ

t =int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ret = ans3(arr)
    print (ret)
