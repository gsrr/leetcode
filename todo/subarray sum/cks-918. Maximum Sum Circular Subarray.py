class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if all(i<=0 for i in A):
            return max(A)
        
        s=0
        small=collections.deque([(0,-1)])
        n=len(A)
        ans=A[0]
        for j,i in enumerate(A*2):
            s+=i
            while small and small[-1][0]>=s:
                small.pop()
            small.append((s,j))
            #print small
            while j-small[0][1]>n:
                small.popleft()
            ans=max(ans,s-small[0][0])
            print small, s, ans
            
        return ans
