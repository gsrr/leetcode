#code

def ans(arr):
    dic = {}
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            dic[arr[i]] = True
    return pow(2, len(dic.keys())) - 1

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(ans(arr))
