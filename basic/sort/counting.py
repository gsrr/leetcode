import main

'''
Sorted character array
input: geeksforgeeks
output: eeeefggkkorss
'''

def get_max_digits(arr):
    gmax = 0
    for i in xrange(len(arr)):
        gmax = max(gmax, len(str(arr[i])))
    return gmax

def radix(arr):
    base = 10
    mdig = get_max_digits(arr)
    for i in xrange(mdig):
        bucket = [ [] for _ in xrange(len(arr))]
        bval = pow(base, i)
        for j in xrange(len(arr)):
            bucket[(arr[j] // bval) % 10].append(arr[j])
        
        cnt = 0
        for j in xrange(len(bucket)):
            for val in bucket[j]:
                arr[cnt] = val
                cnt += 1
    return arr

def ans(arr):
    arr = radix(arr)
    return ",".join( [str(x) for x in arr] )

if __name__ == "__main__":
    main.main(ans)
