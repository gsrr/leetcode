def ans(s, k):
    base = []
    for i in xrange(len(s)):
        if s[i].isalpha():
            base.append(s[i])
        else:
            if len(base) * int(s[i]) >= k:
                break
            base = base * int(s[i])
    #print base
    return base[k % len(base) - 1]

def ans1(s, k):
    arr = list(s)
    st = []
    
    base = 0
    start = 0
    for i in xrange(len(arr)):
        if arr[i].isalpha():
            base += 1
            if base == k:
                return arr[i]
        else:
            val = int(arr[i])
            base *= val
            if base >= k:
                start = i
                base = base / val
                cnt = 1
                tsum = base
                while tsum < k:
                    tsum += base
                    cnt += 1
                base = tsum - base
                st = [(start, cnt - 1)]
                break
    
    return ans1(s, k - base)
    print st, k, base , k - base
    k = k - base
    i = 0
    while i < len(arr):
        #print st
        if arr[i].isalpha():
            #print arr[i],
            k -= 1
            if k == 0:
                return arr[i]
        else:
            if len(st) == 0:
                st.append((i, 1))
            else:
                index, val = st.pop()
                if index == i:
                    val += 1
                    if val == int(arr[i]):
                        i += 1
                        continue
                    st.append((i, val))
                else:
                    st.append((index, val))
                    st.append((i, 1))
            i = -1
        i += 1

class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        return ans1(S, K)
