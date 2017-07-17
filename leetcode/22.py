
def is_valid(arr):
    cnt = 0
    st = []
    for i in xrange(len(arr)):
        if arr[i] == "(":
            st.append(arr[i])
        else:
            cnt += 1
            while len(st) > 0:
                val = st.pop(-1)
                if val == "(":
                    cnt -= 1
                else:
                    cnt += 1
                if cnt == 0:
                    break
            if cnt != 0:
                return False
    return True
    
def jpermutations(arr, s, ret):
    if s == len(arr) - 1:
        if is_valid(arr):
            ret.append("".join(arr))
        return
    hist = {}
    for i in xrange(s, len(arr)):
        if hist.has_key(arr[i]) == False:
            arr[s], arr[i] = arr[i], arr[s]
            jpermutations(arr, s + 1, ret)
            arr[s], arr[i] = arr[i], arr[s]
            hist[arr[i]] = True

def ans(n):
    arr = ["(", ")"] * n
    ret = []
    jpermutations(arr, 0, ret)
    return ret

def generate(n, cnt, ia, ib, tmp, ret):
    if ia == n and ib == n:
        ret.append(tmp)

    if cnt == 0:
        if ia < n:
            generate(n, cnt + 1, ia + 1, ib, tmp + "(", ret)
        else:
            return
    elif cnt > 0:
        if ia < n:
            generate(n ,cnt + 1, ia + 1, ib, tmp + "(", ret)
        if ib < n:
            generate(n, cnt - 1, ia, ib + 1, tmp + ")", ret)
        
def ans_v2(n):
    ret = []
    tmp = ""
    ia, ib = 0, 0
    generate(n, 0, ia, ib, tmp,  ret)
    print ret
    return ret
     
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ans_v2(n)
        
obj = Solution()
obj.generateParenthesis(3)
