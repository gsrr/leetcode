



def ans(nums):
    xorn = 0
    for n in nums:
        xorn = xorn ^ n
    base = 1
    tmp = 0
    cnt = 0
    while tmp == 0:
        tmp = base << cnt
        tmp = tmp & xorn
        cnt += 1
    n1 = [ x for x in nums if x & tmp != 0]
    n2 = [ x for x in nums if x & tmp == 0]

    t1 = 0
    for n in n1:
        t1 = t1 ^ n
    t2 = 0
    for n in n2:
        t2 = t2 ^ n
    
    return [t1, t2]

nums = [1, 2, 1, 3, 2, 5]
#return [3, 5].
print ans(nums)
