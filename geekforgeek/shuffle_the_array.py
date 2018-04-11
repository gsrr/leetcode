
import random


def shuffle_arr(arr):
    print random.randint(0, 1)
    for i in xrange(len(arr) - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def shuffle_arr2(arr):
    print random.randint(0, 1)
    for i in xrange(len(arr)):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = range(100)
print arr
print shuffle_arr(arr)
print shuffle_arr2(arr)
