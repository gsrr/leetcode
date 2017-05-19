def count(num, ret):
    if num == 0:
        return 0
    if ret[num] != 0:
        return ret[num]
    return count(num/2, ret) + num % 2

num = 4
ret = [0] * (num + 1)
for i in xrange(1, num + 1):
       ret[i] =  count(i, ret)

print ret


