def time_plus(t):
    h,m = t.split(":", 1)
    nm = int(m) + 1
    c = nm / 60
    nm = nm % 60
    nh = (int(h) + c) % 24
    return "%s:%s"%(str(nh).zfill(2), str(nm).zfill(2))

class Solution(object):
    def nextClosestTime(self, t):
        """
        :type time: str
        :rtype: str
        """
        tt = str(t)
        stt = set(tt)
        nt = ""
        while True:
            nt = time_plus(tt)
            snt = set(nt)
            if snt.issubset(stt):
                break
            tt = nt
        return nt
