def ans_3(chars):
    '''
    Two variable traverse
    
    Time Complexity : O(n)
    Result : Accept
    '''
    i = 0
    idx = 0
    while i < len(chars):
        j = i + 1
        while j < len(chars):
            if chars[j] != chars[i]:
                break
            else:
                j += 1
        chars[idx] = chars[i]
        idx += 1
        if j - i > 1:
            for nc in str(j - i):
                chars[idx] = nc
                idx += 1
        i = j
    return idx
    
    
def ans_2(chars):
    '''
    Count chars first
    
    Time Complexity : O(n)
    Space Complexity : O(n)
    Result : Accept
    '''
    ret = [[chars[0], 1]]
    for i in xrange(1, len(chars)):
        if chars[i] == ret[-1][0]:
            ret[-1][1] += 1
        else:
            ret.append([chars[i], 1])
    
    idx = 0
    for i in xrange(len(ret)):
        chars[idx] = ret[i][0]
        idx += 1
        if ret[i][1] == 1:
            continue
        for c in str(ret[i][1]):
            chars[idx] = c
            idx += 1
    return idx
    
def ans_1(chars):
    '''
    Traverse array
    
    Time Complexity : O(n)
    Result : Accept
    '''
    c = chars[0]
    cnt = 1
    idx = 0
    for i in xrange(1, len(chars)):
        if chars[i] == c:
            cnt += 1
        else:
            chars[idx] = c
            idx += 1
            if cnt != 1:
                scnt = str(cnt)
                for j in xrange(len(scnt)):
                    chars[idx] = scnt[j]
                    idx += 1
            c = chars[i]
            cnt = 1
    chars[idx] = c
    idx += 1
    if cnt != 1:
        scnt = str(cnt)
        for j in xrange(len(scnt)):
            chars[idx] = scnt[j]
            idx += 1
    return idx

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        return ans_3(chars)
