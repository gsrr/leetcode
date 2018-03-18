class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        cands = ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99", "aa", "bb", "cc", "dd", "ee", "ff"]
        ret = ""
        for i in xrange(1, len(color), 2):
            chex = color[i : i + 2]
            cint = int(chex, 16)
            sim = -0x7fffffff
            tstr = ""
            for c in cands:
                tmp = -1 * (cint - int(c, 16)) * (cint - int(c, 16))
                if tmp > sim:
                    sim = tmp
                    tstr = c
            ret += tstr
        return "#" + ret
