class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = list(str(n))
        cnt = -1
        index = -1
        for i in xrange(len(arr) - 1, -1, -1):
            for j in xrange(i - 1, -1, -1):
                v1 = int(arr[i])
                v2 = int(arr[j])
                if v1 > v2:
                    if j > cnt:
                        index = i
                        cnt = j
                    break

        if cnt == -1:
            return -1
        arr[index], arr[cnt] = arr[cnt], arr[index]
        arr1 = arr[0 : cnt + 1]
        arr2 = arr[cnt + 1:]
        arr2.sort()
        arr1.extend(arr2)
        
        val = 0
        for v in arr1:
            val = val * 10
            val += int(v)
        if val > 0x7fffffff:
            return -1
        return val
