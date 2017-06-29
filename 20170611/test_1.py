import collections

def edge(cnums, e):
    cnt = 0
    if e == 3:
        for key, val in cnums.items():
            if val < 3:
                continue
            total = val * (val - 1) * (val - 2)
            #total = total / 6
            cnt += total
    elif e == 2:
        for key, val in cnums.items():
            if val < 2:
                continue
            total = val * (val - 1)
            #total = total / 2
            for k, v in cnums.items():
                if k == key:
                    continue
                if k >= (key + key):
                    continue
                cnt += (total * v)
    elif e == 1:
        nums = cnums.keys()
        nums.sort()
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                for k in xrange(j + 1, len(nums)):
                    if nums[i] + nums[j] <= nums[k]:
                        break
                    cnt += (cnums[nums[i]] * cnums[nums[j]] * cnums[nums[k]])
    print "test", e, cnt
    return cnt

def triangleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cnums = collections.Counter(nums)
    print cnums
    cnt = 0
    for e in xrange(3, 0, -1):
       cnt += edge(cnums, e) 
       print e, cnt
    return cnt

nums = [2,2,3,4]
nums = [67,86,94,46,81,79,33,74,55,91,96,78,37,32,37,30,94,89,50,20,41,88,64,65,51,26,89,14,11,94,24,53,71,39,14,51,91,33,30,51,41,18,34,15,99,99,24,54,71,38,53,68,40,99,32,24,30,37,62,30,17,88,49,65,61,13,70,12,16,98,70,76,21,100,59,13,50,99,97,86,38,49,27,66,23,29,74,57,63,45,68,85,81,14,96,37,49,68,66,47,43,94,32,89,80,91,94,49,51,100,30,27,99,64,99,49,59,54,78,14,99,16,67,41,90,43,23,41,42,63,27,43,45,65,74,53,99,61,73,49,81,59,43,11,41,69,41,77,92,83,16,74,91,55,13,31,12,79,59,15,79,96,77,24,42,43,47,62,19,40,23,60,81,38,60,10,61,18,55,65,56,53,18,29,53,81,47,95,31,80,94,45,49,39,65,96,80,91,68,67,33,95,35,57,77,37,74,64,51,41,68,26,74,62,59,60,94,81,88,75,47,60,68,33,63,68,80,64,65,19,85,88,46,45,73,81,57,37,51,100,83,65,51,92,22,50,65,40,67,95,86,42,20,50,96,15,70,92,58,37,37,36,89,59,96,55,84,83,69,15,97,20,36,61,74,80,55,95,28,85,80,47,57,26,43,25,11,10,91,83,23,15,17,62,35,68,19,92,25,45,49,81,64,88,24,58,52,26,23,51,61,80,10,10,52,73,17,35,17,40,48,24,27,62,94,89,64,100,99,85,19,30,65,35,11,48,14,79,35,21,10,39,78,48,98,35,40,100,49,36,76,16,65,65,55,30,50,81,65,47,11,18,68,97,19,56,83,32,65,92,68,13,55,34,82,20,20,17,25,35,71,83,35,47,50,89,33,17,60,15,63,88,84,75,80,35,39,28,61,100,12,11,80,98,15,95,44,24,83,37,38,32,47,14,71,50,55,76,41,57,90,60,11,68,74,30,79,90,54,75,95,81,83,37,52,95,56,56,86,84,41,82,43,33,85,68,53,71,76,33,29,10,94,78,61,19,41,42,95,34,45,81,98,96,84,30,35,65,93,78,42,34,76,46,34,62,47,53,71,28,31,68,35,10,60,17,14,58,86,93,38,89,93,68,89,79,81,14,96,28,68,51,21,59,37,46,16,45,18,83,51,67,15,31,69,12,42,60,53,61,89,29,55,99,69,57,50,72,60,39,66,69,21,12,84,63,87,58,85,67,66,39,16,69,86,83,78,45,39,71,51,50,47,19,63,31,41,99,33,58,74,27,57,55,75,22,78,19,90,21,79,27,65,70,87,88,79,83,65,86,18,26,62,23,51,10,90,86,64,47,29,97,54,12,96,77,98,28,70,67,51,90,33,16,83,47,11,74,29,44,98,18,77,39,43,52,54,41,85,46,96,76,25,48,38,27,71,94,49,11,81,67,80,68,84,67,65,54,90,47,51,66,74,95,93,64,54,98,65,77,59,12,70,37,24,84,58,29,96,89,24,27,62,81,94,94,17,39,60,36,49,72,19,20,59,51,76,25,29,68,41,34,63,31,76,80,71,34,61,64,12,37,78,76,99,46,32,44,46,11,45,96,19,79,10,86,33,68,41,18,81,39,72,44,39,26,95,94,25,53,44,45,36,31,60,44,77,21,29,38,35,99,80,50,34,83,62,56,70,79,22,78,31,63,64,44,74,57,42,93,62,39,59,46,95,89,80,90,80,48,77,98,21,13,27,41,19,39,48,24,54,100,20,33,56,21,53,96,10,37,82,16,93,55,75,74,48,46,74,49,54,41,20,34,33,56,96,20,19,46,25,56,14,26,12,25,88,52,47,48,86,73,37,97,75,83,38,77,43,58,69,44,77,80,15,85,62,35,78,82,73,47,10,61,14,53,68,100,18,99,51,98,61,14,79,21,11,36,85,66,100,25,86,36,82,52,66,73,47,16,54,54,12,99,89,38,71,82,89,39,45,92,84,86,40,47,28,38,91,94,51,26,17,84,47,50,68,35,57,99,91,54,98,66,98,85,32,44,93,17,93,39,99,100,46,10,69,63,78,53,28,100,27,37,49,20,94,53,20,37,73,72,96,53,90,13,14,14,60,98,44,83,67,62,51,92,17,15,96,92,83,74,37,35,83,97,27,77,98,73,39,57,73,13,81,75,14,69,97,16,99,29,32,70,92,44,24,97,66,86,82,58,32,57,49,43,59,89,28,72,52,74,30,45,19,82,14,25,98,54,20,92,19,100,69,83,80,84,80,75]
print triangleNumber(nums)