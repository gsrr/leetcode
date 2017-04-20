def next_perm(num):
    for i in range(len(num)-2, -1, -1):
        if num[i] < num[i+1]:
            break
        else:
            num.reverse()
            return num
    for j in range(len(num)-1, i, -1):
        if num[j] > num[i]:
            num[i], num[j] = num[j], num[i]
            break
    for j in range(0, (len(num) - i)//2):
        num[i+j+1], num[len(num)-j-1] = num[len(num)-j-1], num[i+j+1]
    return num

print next_perm([1,2,2,3,3,4,4])
