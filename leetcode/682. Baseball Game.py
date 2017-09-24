

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        if len(ops) == 0:
            return 0
        
        st = []
        for i in xrange(len(ops)):
            if ops[i] == "D":
                if len(st) == 0:
                    continue
                val = st[-1] * 2
                st.append(val)
            elif ops[i] == "C":
                if len(st) == 0:
                    continue
                st.pop()
            elif ops[i] == "+":
                if len(st) == 0:
                    continue
                elif len(st) == 1:
                    val = st[-1]
                    st.append(val)
                else:
                    val = st[-1] + st[-2]
                    st.append(val)
            else:
                st.append(int(ops[i]))
            
        return sum(st)
