def parse(s):
    st = []
    for c in s:
        if c == "#":
            if len(st) != 0:
                st.pop()
        else:
            st.append(c)
    return "".join(st)
    
def ans(S, T):
    fs = parse(S)
    ft = parse(T)
    return fs == ft

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return ans(S, T)
