import bisect


def ans1(difficulty, profit, worker):
    arr = []
    for i in xrange(len(difficulty)):
        arr.append((difficulty[i], profit[i]))
    arr.sort(key=lambda x: x[0])
    new_diff = [ x[0] for x in arr ]
    new_prof = [ x[1] for x in arr ]

    total = 0
    for i in xrange(len(worker)):
        idx = bisect.bisect_right(new_diff, worker[i])
        tmp = 0
        for j in xrange(idx - 1 , -1, -1):
            if new_prof[j] > tmp:
                tmp = new_prof[j]
        total += tmp
    return total

def ans(difficulty, profit, worker):
    arr = []
    for i in xrange(len(difficulty)):
        arr.append((difficulty[i], profit[i]))
    arr.sort(key=lambda x: x[0])
    new_diff = [ x[0] for x in arr ]
    new_prof = [ x[1] for x in arr ]
    max_prof = [0] * len(new_prof)
    mval = 0
    for i in xrange(len(new_prof)):
        if new_prof[i] > mval:
            mval = new_prof[i]
        max_prof[i] = mval

    print max_prof
    total = 0
    for i in xrange(len(worker)):
        idx = bisect.bisect_right(new_diff, worker[i])
        if idx != 0:
            total += (max_prof[idx - 1])
            print idx, total, max_prof[idx - 1]
    return total

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        return ans(difficulty, profit, worker)




difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]
s = Solution()
print s.maxProfitAssignment(difficulty, profit, worker)

