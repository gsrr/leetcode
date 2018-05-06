def remove_para(S):
    ret = []
    for i in xrange(len(S)):
        if S[i] != "(" and S[i] != ")" and S[i] != "-" and S[i] != " ":
            ret.append(S[i])
    return "".join(ret)    

def phone(S):
    '''
    1. The last 10 digits make up the local number 
    '''
    S = remove_para(S)
    print S
    if S[0] == "+" or S[0] == "-":
        if len(S) <= 11:
            return "***-***-" + S[-4:] 
                

    if len(S) <= 10:
        return "***-***-" + S[-4:] 
    else:
        lcs = len(S) - 10
        print lcs
        if S[0] == "-":
            lcs -= 1
            return "-" + "*"*lcs + "-***-***-" + S[-4:]
        elif S[0] == "+":
            lcs -= 1
            return "+" + "*"*lcs + "-***-***-" + S[-4:]
        else:
            return "+" + "*"*lcs + "-***-***-" + S[-4:]
        
    return S

def email(S):
    '''
    1. all names must be converted to lowercase
    2. all letters between the first and last letter of the first name
    '''
    S = S.lower()
    str1, str2 = S.split("@", 1)
    str1 = "".join([str1[0], "*****", str1[-1]])
    return "@".join([str1, str2])    

class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if "@" in S:
            return email(S) 
        else:
            return phone(S)
        

s = Solution()
ex = "LeetCode@LeetCode.com"
print s.maskPII(ex)
ex = "AB@qq.com"
print s.maskPII(ex)
ex = "1(234)567-890"
print s.maskPII(ex)
ex = "86-(10)12345678"
print s.maskPII(ex)
ex = "+(501321)-50-23431"
print s.maskPII(ex)
ex = "+46(427)55-7-41"
print s.maskPII(ex)
ex = "(3906)2 07143 711"
print s.maskPII(ex)
