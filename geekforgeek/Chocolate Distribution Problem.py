#code
import itertools

def ans_sort(arr, m):
    '''
    sorting method
    Time complexity : O(nlogn)
    '''
    min_diff = 0x7fffffff
    arr.sort()
    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])
    return min_diff

def ans_comb(arr, m):
    '''
    combination of itertools
    Result : Time Limit Exceeded
    Time complexity : O(5 * Comb(n, m))
    '''
    if m == 1:
        return 0
    min_diff = 0x7fffffff
    for line in itertools.combinations(arr, m):
        min_diff = min(min_diff, max(line) - min(line))
    return min_diff

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    print(ans(arr, m))
