#!/bin/python

import sys

def raceAgainstTime(n, mh, heights, prices, st):
    # Complete this function
    dp = [0] * (n - 1)
    for i in xrange(len(dp) - 1, -1, -1):
        minval = len(dp) - i

        for j in xrange(i + 1, len(dp)):
            if heights[j] > heights[i]:
                minval = heights[j] - heights[i] + prices[j] + (j - i) + dp[j]
                break

        for j in xrange(i + 1, len(dp)):
            if heights[j] > heights[i]:
                break
            else:
                if prices[j] >= 0:
                    continue
                cost = heights[i] - heights[j] + prices[j] + (j - i) + dp[j]
                if cost <= minval:
                    minval = cost
        dp[i] = minval         
    #print dp
    current_height = mh
    minval = len(dp) - (-1)

    for i in xrange(0, len(dp)):
            if heights[i] > mh:
                minval = heights[i] - mh + prices[i] + (i - (-1)) + dp[i] 
                break

    for i in xrange(len(dp)):
        if heights[i] > mh:
            break
        else:
            if prices[i] >= 0:
                continue
            cost = mh - heights[i] + prices[i] + (i - (-1)) + dp[i] 
            if cost <= minval:
                minval = cost
    return minval
    
if __name__ == "__main__":
    n = int(raw_input().strip())
    mason_height = int(raw_input().strip())
    heights = map(int, raw_input().strip().split(' '))
    prices = map(int, raw_input().strip().split(' '))
    result = raceAgainstTime(n, mason_height, heights, prices, 0)
    print result

