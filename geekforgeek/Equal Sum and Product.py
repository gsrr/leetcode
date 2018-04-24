#code

def ans(arr):
    cnt = len(arr)
    for i in range(len(arr)):
        sumi = arr[i]
        multi = arr[i]
        for j in range(i + 1, len(arr)):
            sumi += arr[j]
            multi *= arr[j]
            if sumi == multi:
                cnt += 1
    return cnt

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(ans(arr))
