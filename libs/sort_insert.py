import random as rand

# min_arr = [(0x7fffffff, 0)] == [(val, index)]
def insert_with_index(min_arr, elem):
    j = len(min_arr) - 1
    min_arr[j] = elem
    while j > 0:
        if min_arr[j] > min_arr[j - 1]:
            break
        else:
            min_arr[j], min_arr[j - 1] = min_arr[j - 1], min_arr[j]
            j -= 1


def test_insert_with_index():
    arr = [ rand.randint(10,100) for x in xrange(10) ]
    min_arr = [(0x7fffffff, 0)] * 10
    print "Before sorting:", arr
    print "Before sorting:", min_arr
    for i in xrange(len(arr)):
        insert_with_index(min_arr, (arr[i], i))
    print "After Sorting:", min_arr

test_insert_with_index()


