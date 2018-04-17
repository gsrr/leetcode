import decimal

# create a new context for this task
ctx = decimal.Context()

# 20 digits should be enough for everyone :D
ctx.prec = 20

def float_to_str(f):
    """
    Convert the given float to a string,
    without resorting to scientific notation
    """
    d1 = ctx.create_decimal(repr(f))
    return format(d1, 'f')

def is_valid(pair):
    v1 = pair[0]
    v2 = pair[1]
    for v in [v1, v2]:
        if len(v) == 1:
            continue
        if v[0] == 0:
            return False
    return True

def collect(ret, left, right):
    if len(left) == 0 or len(right) == 0:
        return
    
    if len(left) != 1:
        if left[0] == '0' and left[-1] == '0':
            return
    if len(right) != 1:
        if right[0] == '0' and right[-1] == '0':
            return
    
    lval = 0
    for i in xrange(len(left)):
        lval = lval * 10
        lval += int(left[i])
    
    if lval == 0 and len(left) != 1:
        return
    
    rval = 0
    for i in xrange(len(right)):
        rval = rval * 10
        rval += int(right[i])
    
    if rval == 0 and len(right) != 1:
        return
    
    if left[0] == "0" and right[0] == "0":
        if lval != 0:
            lval = lval / float(pow(10, len(left) - 1))
        if rval != 0:
            rval = rval / float(pow(10, len(right) - 1))
        ret.append("(%s, %s)"%(float_to_str(lval), float_to_str(rval)))
        return
    
    if left[0] == "0" and right[0] != "0":
        if lval != 0:
            lval = lval / float(pow(10, len(left) - 1))
        rbase = 1
        for i in xrange(len(right)):
            rval = rval / rbase
            if i != 0:
                rval = round(rval, i)
            ret.append("(%s, %s)"%(float_to_str(lval), float_to_str(rval)))
            rbase = 10.0
            if right[-1] == "0":
                return
        return
    
    if right[0] == "0" and left[0] != "0":
        if rval != 0:
            rval = rval / float(pow(10, len(right) - 1))
        lbase = 1
        for i in xrange(len(left)):
            lval = lval / lbase
            if i != 0:
                lval = round(lval, i)
            ret.append("(%s, %s)"%(float_to_str(lval), float_to_str(rval)))
            lbase = 10.0
            if left[-1] == "0":
                return
        return
    
    lbase = 1
    for i in xrange(len(left)):
        lval = lval / lbase
        rbase = 1
        tval = rval
        lbase = 10.0
        for j in xrange(len(right)):
            tval = tval / rbase
            if i != 0:
                lval = round(lval, i)
            if j != 0:
                tval = round(tval, j)
            ret.append("(%s, %s)"%(float_to_str(lval), float_to_str(tval)))
            rbase = 10.0
            if right[-1] == "0":
                break
        if left[-1] == "0":
            return
    return

def ans1(ss):
    ss = ss.strip("()")
    ret = []
    left = []
    right = list(ss)
    for i in xrange(len(ss)):
        left.append(ss[i])
        right.pop(0)
        collect(ret, left, right)
    return ret
    
class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        return ans1(S)
