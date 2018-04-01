def stretchy(str1, str2):
    sc1 = 0
    ec1 = 0
    sc2 = 0
    ec2 = 0
    while sc1 < len(str1) and sc2 < len(str2):
        if str1[sc1] != str2[sc2]:
            return 0
        
        while ec1 < len(str1) and str1[ec1] == str1[sc1] :
            ec1 += 1
        while ec2 < len(str2) and str2[ec2] == str2[sc2] :
            ec2 += 1
        
        cnt1 = ec1 - sc1
        cnt2 = ec2 - sc2
        if cnt2 > cnt1:
            return 0
        if cnt1 != cnt2:
            #if cnt1 - 2 < cnt2:
                #return 0
            if cnt1 < 3:
                return 0
        sc1 = ec1
        sc2 = ec2
    if sc1 != len(str1) or sc2 != len(str2):
        return 0
    return 1
            
class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        cnt = 0
        for w in words:
            cnt += stretchy(S, w)
        return cnt
        
