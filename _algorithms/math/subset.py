
ret1 = 0

def ans1(nums, i, val):
    global ret1
    if len(nums) == i:
        ret1 += val
        return
    ans1(nums, i + 1, val)
    ans1(nums, i + 1, val + nums[i])
    

def sumofsubset(nums):  
    global ret1
    ret1 = 00
    ans1(nums, 0, 0) 
    print ret1
    
    
sumofsubset([1,2,3])
