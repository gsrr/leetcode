import collections

def ans(words):
    mose = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    hist = collections.defaultdict(int)
    for w in words:
        rst = ""
        for c in w:
            rst += mose[ord(c) - ord('a')]
        hist[rst] += 1
    return len(hist.keys())

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        return ans(words)
