import collections

def ans_3(letters, target):
    nletters = collections.Counter(letters).keys()
    return ans_1(nletters, target)

def ans_2(letters, target):
    dic = collections.Counter(letters)
    for i in xrange(1, 27):
        n = (ord(target) - ord('a') + i) % 26
        nc = chr(n + ord('a'))
        if dic.has_key(nc):
            return nc

def ans_1(letters, target):
    letters.sort()
    for c in letters:
        if c > target:
            return c
    return letters[0]

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        return ans_1(letters, target)
        
