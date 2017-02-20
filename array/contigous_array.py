def findMaxLength(nums):
    sums = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        if nums[i] == 0:
            sums[i + 1 ] = sums[i] - 1
        else:
            sums[i + 1 ] = sums[i] + 1
    
    print sums
    map_dic = {}
    for i in range(len(nums) + 1):
        if map_dic.has_key(sums[i]) == False:
            map_dic[sums[i]] = []
        map_dic[sums[i]].append(i)

    print map_dic
    answer = 0
    for key in map_dic.keys():
        l = map_dic[key]
        answer = max(answer, l[len(l) - 1] - l[0])
    print answer
findMaxLength([0,0,0,1,0,1])
findMaxLength([0,1])
findMaxLength([0,1,1,1,0,0, 1])
