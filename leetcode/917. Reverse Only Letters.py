def ans(S):
    arr = list(S)
    ret = []
    i = 0
    j = len(arr) - 1
    while i < len(arr):
        if arr[i].isalpha() == False:
            ret.append(arr[i])
            i += 1
        else:
            while j > -1:
                if arr[j].isalpha():
                    ret.append(arr[j])
                    i += 1
                    j -= 1
                    break
                else:
                    j -= 1
    #print ret
    return "".join(ret)
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        return ans(S)
        
