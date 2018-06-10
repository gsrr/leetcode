ns(seats):
    arr = [20000] * len(seats)
    i = 0
    while i < len(seats):
        if seats[i] == 1:
            arr[i] = 0
            j = i + 1
            while j < len(seats):
                if seats[j] == 1:
                    break
                else:
                    arr[j] = min(arr[j], j - i)
                    j += 1
            i = j
        else:
            i += 1
    
    i = len(seats) - 1
    while i > -1:
        if seats[i] == 1:
            arr[i] = 0
            j = i - 1
            while j > -1:
                if seats[j] == 1:
                    break
                else:
                    arr[j] = min(arr[j], i - j)
                    j -= 1
            i = j
        else:
            i -= 1
    return max(arr)

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        return ans(seats)
