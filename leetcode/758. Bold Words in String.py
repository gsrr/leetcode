'''
tag : kmp,string_matching
'''

def get_failure_func(word):
    dp = [-1] * len(word)
    for i in xrange(1, len(word)):
        j = dp[i - 1]
        while j > -1 and word[j + 1] != word[i]:
            j = dp[j]
            
        if word[j + 1] == word[i]:
            dp[i] = j + 1
    return dp

def kmp_search(word, S):
    ret = []
    ff = get_failure_func(word)
    i = 0
    j = 0
    while i < len(S):
        if j == len(word):
            ret.append([i - j, i]) # [start in front, end in rear]  
            j = ff[j - 1] + 1
            
        if S[i] == word[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = ff[j - 1] + 1
    if j == len(word):
        ret.append([i - j, i]) # [start in front, end in rear]  
    return ret
    
def find_occur_ans2(words, S):
    bold_list = []
    for w in words:
        bold_list.extend(kmp_search(w, S))
    return bold_list
        
def find_occur_ans1(words, S):
    '''
    1. String matching
    '''
    bold_list = []
    for w in words:
        sp = 0
        sw = S.find(w, sp)
        while sw >= 0:
            sp = sw + 1
            bold_list.append([sw, sw + len(w)]) # [start in front, end in rear]
            sw = S.find(w, sp)
    return bold_list

def combine_interval(bold_list):
    new_list = [[bold_list[0][0], bold_list[0][1]]]
    for i in xrange(1, len(bold_list)):
        psp = new_list[-1][0]
        pep = new_list[-1][1]
        sp = bold_list[i][0]
        ep = bold_list[i][1]
        if ep <= pep:
            continue
        if sp <= pep:
            new_list[-1][1] = ep
        else:
            new_list.append([sp, ep])
    return new_list

def insert_bold_ans1(new_list, S):
    '''
    Time : 88 ms
    '''
    new_str = []
    ret = list(S)
    for i in xrange(len(new_list)):
        p1 = 2 * i + new_list[i][0]
        p2 = 2 * i + new_list[i][1] + 1
        ret.insert(p1, "<b>")
        ret.insert(p2, "</b>")
    sret = "".join(ret)
    return sret

def insert_bold_ans2(new_list, S):
    '''
    Time : 65 ms
    '''
    ret = []
    cnt = 0
    for i in xrange(len(new_list)):
        sp = new_list[i][0]
        ep = new_list[i][1]
        while cnt < sp:
            ret.append(S[cnt])
            cnt += 1
        ret.append("<b>")
        while cnt < ep:
            ret.append(S[cnt])
            cnt += 1
        ret.append("</b>")
        
    while cnt < len(S):
        ret.append(S[cnt])
        cnt += 1
    return "".join(ret)

def insert_bold_ans3(new_list, S):
    '''
    Time : 58 ms
    '''
    ret = []
    cnt = 0
    for i in xrange(len(new_list)):
        sp = new_list[i][0]
        ep = new_list[i][1]
        ret.extend([S[cnt:sp], "<b>", S[sp:ep], "</b>"])
        cnt = ep
    ret.append(S[cnt:])
    return "".join(ret)

def ans_1(words, S):
    bold_list = find_occur_ans2(words, S)
    if len(bold_list) == 0:
        return S

    bold_list.sort()
    new_list = combine_interval(bold_list)
    return insert_bold_ans3(new_list, S)
    
    
class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        return ans_1(words, S)
        
