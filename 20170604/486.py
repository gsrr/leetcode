



def ans(nums, s, e, is_max_player, hist):
    if s == e:
        all_score = sum(nums)
        cur_score = hist + nums[s]
        if (all_score - cur_score) <= cur_score:
            return True
        else:
            return False
    ret = None
    if is_max_player == True:
        ret = False
    else:
        ret = True
    for n in [s , e]:
        ns = s
        ne = e
        if n == s: 
            ns += 1
        else:
            ne -= 1
        if is_max_player == True:
            score = ans(nums, ns, ne ,False, hist + nums[n])
            ret = max(ret, score)
            if ret == True:
                return ret
        else:
            score = ans(nums, ns, ne, True, hist)
            ret = min(ret, score)
            if ret == False:
                return ret
    return ret

hist = 0
nums = [1,2,233,5]
print ans(nums, 0, len(nums) - 1, True, hist)
nums = [2,233,5]
print ans(nums, 0, len(nums) - 1, True, hist)
nums = [1,567,1,1]
print ans(nums, 0, len(nums) - 1, True, hist)
