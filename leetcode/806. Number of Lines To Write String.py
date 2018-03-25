def ans(arr, S):
    cnt = 0
    summ = 0
    for c in S:
        summ += arr[ord(c) - 97]
        if summ > 100:
            summ = arr[ord(c) - 97]
            cnt += 1
        elif summ == 100:
            summ = 0
            cnt += 1
    return [cnt + 1, summ]


class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        return ans(widths, S)
