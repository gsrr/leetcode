def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def ans(nums):
    cnt = 0
    maxval = 0
    for i in nums:
        if i == 0:
            maxval = cnt if cnt > maxval else maxval
            cnt = 0
        else:
            cnt += 1
    maxval = cnt if cnt > maxval else maxval
    return maxval

cases = [
    [[1,1,0,1,1,1]]
]
test(cases,1)

