def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def ans(nums):
    print nums
    cnt = 0
    for i in xrange(len(nums)):
        if nums[i] != 0:
            nums[cnt] = nums[i]
            cnt += 1
    for j in xrange(cnt, len(nums)):
        nums[j] = 0
    return nums

cases = [
    [[0, 1, 0, 3, 2]],
    [[]],
]
test(cases,10)

