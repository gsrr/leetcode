def findMax_2(diffArr):
    if len(diffArr) <= 0:
        return 0
    
    max_val = 0
    s = 0
    for i in xrange(len(diffArr)):
        s += diffArr[i]
        if s < 0:
            s = 0
        max_val = max(max_val, s)
    return max_val

def findMax(arr):
    if len(arr) <= 1:
        return 0
    
    diffArr = [arr[i] - arr[i-1] for i in xrange(1, len(arr))]
    max_val = 0
    s = 0
    for i in xrange(len(diffArr)):
        s += diffArr[i]
        if s < 0:
            s = 0
        max_val = max(max_val, s)
    return max_val

def ans_6(prices, k):
    '''
    Inspired from ans_5, 
    1. create a array with element : [hold, release]
    
    Time Complexity : O(n)
    Space Complexity : O(1)
    Result : Accept
    '''
    arr = [[-0x80000000, 0] for _ in xrange(k)]
    arr.append([0, 0])
    for p in prices:
        for i in xrange(k):
            arr[i][1] = max(arr[i][1], arr[i][0] + p)
            arr[i][0] = max(arr[i][0], arr[i + 1][1] - p)
    return arr[0][1]
    
def ans_5(prices):
    '''
    From discussion area (Dynamic programming)
    
    Time Complexity : O(n)
    Space Complexity : O(1)
    Result : Accept
    '''
    hold1 = -0x80000000
    hold2 = -0x80000000
    release1 = 0
    release2 = 0
    for p in prices:
        print (hold1, release1, hold2, release2)
        release2 = max(release2, hold2 + p)
        hold2 = max(hold2, release1 - p)   # buy hold-2
        release1 = max(release1, hold1 + p)  # sell hold-1
        hold1 = max(hold1, -p) # buy hold-1
    return release2

def ans_4(prices):
    '''
    Create two arrays:
    --> One from left to right, store max profit for each subarray (lr_arr, lenght)
    --> One from right to left, store max profi for each subarray (rl_arr, length + 2)
    Summation for lr_arr[i] + lr_arr[i + 2]
    
    Time Complexity : O(n)
    Result : Accept
    '''
    diffArr = [prices[i] - prices[i-1] for i in xrange(1, len(prices))]
    lr_arr = [0] * len(diffArr)
    rl_arr = [0] * (len(diffArr) + 2)
    max_val = 0
    s = 0
    for i in xrange(len(diffArr)):
        s += diffArr[i]
        if s < 0:
            s = 0
        max_val = max(max_val, s)
        lr_arr[i] = max_val

    s = 0
    max_val = 0
    for i in xrange(len(diffArr) - 1, -1, -1):
        s += diffArr[i]
        if s < 0:
            s = 0
        max_val = max(max_val, s)
        rl_arr[i] = max_val
    
    max_val = 0
    for i in xrange(len(lr_arr)):
        max_val = max(max_val, lr_arr[i] + rl_arr[i + 2])
    
    return max_val
    
    
def ans_3(prices):
    '''
    ans_2 enhancement - without diffArr in findMax
    
    Time Complexity : O(n^2)
    Result : Time Limit Exceeded
    '''
    diffArr = [prices[i] - prices[i-1] for i in xrange(1, len(prices))]
    max_val = 0
    for i in xrange(len(diffArr)):
        
        tval = findMax_2(diffArr[0:i]) + findMax_2(diffArr[i:])
        if tval > max_val:
            max_val = tval
    return max_val

def ans_2(prices):
    '''
    Double Recursive
    
    Time Complexity : O(n^2)
    Result : Time Limit Exceeded
    '''
    max_val = 0
    for i in xrange(len(prices)):
        max_val = max(max_val, findMax(prices[0:i]) + findMax(prices[i:]))
    return max_val
    
def ans_1(prices):
    '''
    Recursive
    
    Time Complexity : O(n^3)
    Result : Time Limit Exceeded
    
    '''
    max_val = 0
    for i in xrange(len(prices)):
        for j in xrange(i + 1, len(prices)):
            tval = prices[j] - prices[i]
            max_val = max(max_val, tval + findMax(prices[j + 1:]))
    return max_val


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        
        return ans_6(prices, 2)
