import random

# n:int
def create_int_array(n):
    return [random.randint(-100,100) for r in xrange(n)]    
def test_create_int_array():
    print create_int_array(10) 

def find_maximum_sum_subarray(arr):
    print arr
    tmp_sum = 0
    max_sum = 0
    start = 0
    tmp_start = 0
    end = 0
    for i in range(len(arr)):
        tmp_sum += arr[i]
        if tmp_sum < 0:
            tmp_sum = 0
            tmp_start = i + 1
        if tmp_sum > max_sum:
            start = tmp_start
            end = i
            max_sum = tmp_sum
    print "start=%d, end=%d, max_sum=%d"%(start, end, max_sum)
    return max_sum

def main():
    arr1 = [100, -28, -52, -11, -54, -23, -13, 84, -2, 19]
    find_maximum_sum_subarray(arr1)


if __name__ == "__main__":
    main()
