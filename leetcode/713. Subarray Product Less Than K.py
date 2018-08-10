def ans(arr, k):
    '''
    Result : Time Exceed
    Time Complexity : O(n^2)
    '''
    cnt = 0
    for i in xrange(len(arr)):
        psum = 1
        for j in xrange(i, len(arr)):
            psum *= arr[j]
            if psum < k:
                cnt += 1
            else:
                break
    return cnt


from collections import deque
def count(n):
    return (n * (n + 1)) / 2 

def ans1(arr, k):
    if k == 0:
        return 0
    if k == 1:
        return 0
    
    cnt = 0
    #st = deque([])
    st = []
    psum = 1
    for i in xrange(len(arr)):
        psum = psum * arr[i]
        st.append(arr[i])
        while psum >= k:
            cnt += (len(st) - 1)
            val = st.pop(0)
            psum = psum / val
    
    cnt += count(len(st))
    return cnt

def ans2(arr, k):
    if k == 0:
        return 0
    if k == 1:
        return 0
    
    cnt = 0
    s = 0
    psum = 1
    for i in xrange(len(arr)):
        psum = psum * arr[i]
        while psum >= k:
            cnt += (i - s)
            val = arr[s]
            s += 1
            psum = psum / val
    
    cnt += count(len(arr) - s)
    return cnt

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return ans2(nums, k)
