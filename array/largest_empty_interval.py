import random


# n:int
def create_01_array(n):
    return [random.randint(0,1) for r in xrange(n)]    

def test_create_01_array():
    array01 = create_01_array(10)
    array02 = create_01_array(100)
    print array01
    print array02

# 0 is block , 1 is write

def find_largest_empty_interval(arr):
    print arr
    max_length = 0
    cnt = 0
    for i in arr:
        if i == 0:
            max_length = max(max_length, cnt)
            cnt = 0
        else:
            cnt += 1
    max_length = max(max_length, cnt)
    print max_length
    return max_length

def main():
    arr = create_01_array(10)
    print arr
    arr1 = [0, 0, 0, 0, 1, 0, 0, 1, 0, 0] #ans = 1
    ret = find_largest_empty_interval(arr1)
    arr2 = [1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
    ret = find_largest_empty_interval(arr2)
    arr3 = [1, 0, 0, 1, 1, 0, 1, 1, 1, 1]
    ret = find_largest_empty_interval(arr3)


if __name__ == "__main__":
    main()
