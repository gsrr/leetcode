class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
                 
        st = []
        for i in xrange(len(s)):
            if s[i] == ")":
                if len(st) == 0:
                    return False
                if st[-1] == ")":
                    return False
                if st[-1] == "(":
                    st.pop()
                else:
                    find = False
                    for j in xrange(len(st) - 1, -1, -1):
                        if st[j] == "(":
                            st.pop(j)
                            find = True
                            break
                    if find == False:
                        st.pop()
            else:
                st.append(s[i])
        print st
        while len(st) != 0:
            item = st.pop()
            if item == "(":
                return False
            else:
                find = False
                for i in xrange(len(st) - 1, -1, -1):
                    if st[i] == "(":
                        st.pop(i)
                        find = True
                        break
                
        return True
