#code
import heapq

def ans1(arr, k):
    arr.sort()
    return arr[k - 1]

def ans2(arr, k):
    heapq.heapify(arr)
    val = heapq.heappop(arr)
    while k != 1:
        val = heapq.heappop(arr)
        k -= 1
    return val

def ans3(arr, k):
    pivot = arr[0]
    p1 = []
    p2 = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            p1.append(arr[i])
        else:
            p2.append(arr[i])
    
    if k - 1 == len(p1):
        return pivot
    
    if k - 1 > len(p1):
        return ans3(p2, k - 1 - len(p1))
    else:
        return ans3(p1, k)
        
T = int(input())
for _ in range(T):
    N = int(input())
    Arr = list(map(int, input().split()))
    K = int(input())
    print (ans3(Arr, K))
