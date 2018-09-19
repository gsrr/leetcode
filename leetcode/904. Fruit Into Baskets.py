import collections
def ans(arr):
    s = 0
    e = 0
    length = 0
    dic = collections.defaultdict(int)
    while e < len(arr):
        dic[arr[e]] += 1
        e += 1
        while len(dic.keys()) > 2:
            dic[arr[s]] -= 1
            if dic[arr[s]] == 0:
                del dic[arr[s]]
            s += 1
        length = max(length, e - s)
    return length

class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        return ans(tree)
