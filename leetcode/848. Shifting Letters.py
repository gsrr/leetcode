def ans(s, arr):
    for i in xrange(1, len(arr)):
        arr[i] += arr[i - 1]
    #print arr
    ret = []
    for i in xrange(len(s)):
        val = ord(s[i]) - ord('a')
        if i == 0:
            val += arr[-1]
        else:
            val += (arr[-1] - arr[i - 1])
        val %= 26
        val += 97
        ret.append(chr(val))
    return "".join(ret)
    
class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        return ans(S, shifts)
