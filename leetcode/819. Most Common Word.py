 import re
import collections

def ans1(paragraph, banned):
    tokens = re.findall(r"[\w']+", paragraph)
    ctokens = collections.Counter([ x.lower() for x in tokens])
    print ctokens
    for key in ctokens.most_common():
        if key[0] in banned:
            continue
        return key[0]
    return ""

def ans2(paragraph, banned):
    tokens = paragraph.split()
    print tokens
    t2 = [x.strip("!?',;.").lower() for x in tokens]
    ct = collections.Counter(t2)
    for key in ct.most_common():
        if key[0] in banned:
            continue
        return key[0]
    return ""
    
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        return ans2(paragraph, banned)
        
