def prefix_function(s):
    '''
    ex1 : abcdabcd --> [-1, -1, -1, -1, 0, 1, 2, 3]
    ex2 : abcdabcdabcdabcd --> [-1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    abcdabcdabcdabcd
    a
    ab
    abc
    abcd
    abcda
    abcdab
    abcdabc
    abcdabcd
    abcdabcda
    abcdabcdab
    abcdabcdabc
    abcdabcdabcd
    
    ex3 : abcdabefgabcdabab --> [-1, -1, -1, -1, 0, 1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 0, 1]
    abcdabefgabcdabab
    a
    ab
         a
         ab
         abc
         abcd
         abcda
         abcdab
               a
               ab
    '''
    f = [-1] * len(s)
    for i in xrange(1, len(f)):
        f[i] = -1
        j = f[i - 1]
        if s[i] == s[j + 1]:
            f[i] = j + 1
        else:
            while j > -1:
                j = f[j]
                if s[i] == s[j + 1]:
                    f[i] = j + 1
    return f

def prefix_function2(s):
    '''
    longest common prefix function
    '''
    print s
    f = [-1] * len(s)
    for i in xrange(1, len(f)):
        j = f[i - 1]
        while j > -1 and s[i] != s[j + 1]:
            j = f[j]
            
        if s[i] == s[j + 1]:
            f[i] = j + 1
    prefix = []
    for i in xrange(len(f)):
        if f[i] != -1:
            prefix.append(s[0:f[i] + 1])
            print " " * (i - 1 - f[i]), s[0:f[i] + 1]
    return f

def prefix_function3(s):
    '''
    longest common prefix function
    '''
    f = [-1] * len(s)
    for i in xrange(1, len(f)):
        j = f[i - 1]
        while j > -1 and s[i] != s[j + 1]:
            j = f[j]
            
        if s[i] == s[j + 1]:
            f[i] = j + 1
    return f

def test_prefix():
    pref = prefix_function2("abcdabefgabcdabab")
    print pref
    pref = prefix_function2("abcdabcdabcdabcd")
    print pref
    
    
# find str2 in str1
def issub(str1, str2, s):
    i = 0
    while i < len(str2):
        if str1[s + i] != str2[i]:
            break
        i += 1
    return i

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #test_prefix()
        if needle == "":
            return 0
    
        pref = prefix_function3(needle)
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = pref[j - 1] + 1
        return i - j if j == len(needle) else -1
        
