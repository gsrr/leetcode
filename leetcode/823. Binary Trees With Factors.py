'''
Method1
這個問題直覺想法就是bottom-up的暴力法方式.
一個兩個for loop的方式, 但會遇到一個問題,
那就是新增加的值要如何再與前面的值相乘?
(append? 那會造成list亂掉, 所以只好新增一個新的list來儲存)
然後重跑迴圈, 繼續將這個list互乘, 直到list不會再增加為止.

Method2
感覺只是對array裡面的值一直在互乘而已, 所以用dictionary來存次數.

Method3
感覺並不需要新的dp, 也就是可以拿掉外面迴圈.
(但array需要先sort, 這樣的話, 前面乘就代表該值已經固定了)
ex: 若6之前的人都已經乘完, 那代表6最多就是目前這個次數.
所以就從6開始乘所有的人即可
不對, 後面做的會影響前面 --> 像3 * 2 = 6, 6 * 2 = 12這個case就算不到.
[2, 3, 6, 12]
其實可以用遞迴: 12 = (2 * 6), 所以只要確認6的方法數.
而6 = (2 * 3), (3 * 2)
Top - Down method.
'''


import collections

def ans1(arr):
    '''
    Brute force method
    Result : Time expired
    Time complexity: O(logn * n^2)
        The inner loop is n^2 + (n + n/2) * (n + n/2) + (n + n/2 + n/4) * (n + n/2 + n/4) + ...--> O(n^2)
        The outer loop is logn because minval is 2, so the candidate will be remove half at least for every loop.
    Space complexity : O(n^2) in dictionary to store pairs.
    '''
    dic = collections.Counter(arr)
    arr.sort()
    base = list(arr)
    pre = 0
    cur = len(base)
    while pre != cur:
            tmp = []
            n = len(base)
            #print base
            for i in xrange(n):
                    for j in xrange(n):
                            v1 = base[i]
                            v2 = base[j]
                            if dic.has_key(v1 * v2):
                                    tmp.append(v1 * v2)
            pre = cur
            base = arr + tmp
            cur = len(base)
    return len(base)

def ans2(arr):
    '''
    Speedup from brute force method
    Result : Accept
    Time complexity :
        Outer loop : O(logn)
        Inner loop : n/2 * n/2 + n/2 * n/2 + ... --> O(n^2)
    '''
    base = 10 ** 9 + 7
    arr.sort()
    dp = collections.Counter(arr)
    cands = []
    for i in xrange(len(arr)):
            for j in xrange(len(arr)):
                    v1 = arr[i]
                    v2 = arr[j]
                    val = v1 * v2
                    if val > arr[-1]:
                            break
                    if dp.has_key(v1 * v2):
                            cands.append([v1, v2])
    pre = 0
    cur = len(arr)
    cnt = 0
    while pre != cur:
            pre = cur
            cur = 0
            ndp = {}
            for cand in cands:
                    v1 = cand[0]
                    v2 = cand[1]
                    val = (v1 * v2 )
                    if ndp.has_key(val) == False:
                            ndp[val] = (dp[v1] * dp[v2])
                    else:
                            ndp[val] += (dp[v1] * dp[v2])
                    ndp[val] = ndp[val] % base
            for i in xrange(len(arr)):
                    if ndp.has_key(arr[i]) == False:
                            ndp[arr[i]] = 0
                    ndp[arr[i]] += 1
                    cur += ndp[arr[i]]
            dp = ndp
            cnt += 1
    return sum(dp.values()) % base

def ans(arr):
    '''
    Speedup from brute force method
    Result : Accept
    Time complexity :
        Outer loop : O(logn)
        Inner loop : n/2 * n/2 + n/2 * n/2 + ... --> O(n^2)
    '''
    base = 10 ** 9 + 7
    arr.sort()
    dp = collections.Counter(arr)
    print arr
    for i in xrange(len(arr)):
            for j in xrange(len(arr)):
                    v1 = arr[i]
                    v2 = arr[j]
                    val = v1 * v2
                    if val > arr[-1]:
                            break
                    if dp.has_key(v1 * v2):
                            print v1, v2
                            dp[val] += (dp[v1] * dp[v2])  
    print dp
    return sum(dp.values()) % base

class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return ans2(A)
        
