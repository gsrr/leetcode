def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def factor(n):
    ret = []
    cnt = 1
    while cnt * cnt <= n:
        if n % cnt == 0:
            ret.append(cnt)
        cnt += 1
    return ret

def ans(nums, target):
    for i in xrange(len(nums)):
        if nums[i] > target:
            break
        for j in xrange(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i + 1,j + 1]
            if nums[i] == nums[j]:
                break
            if nums[j] > target:
                break
            if nums[i] + nums[j] > target:
                break

cases = [
    [[2, 7, 11, 15], 9],
    [[-1, 0], -1],
    [[0, 0], 0],
    [[0,0,0,0,0,0,0,5], 5]
]
test(cases,1)

