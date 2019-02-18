import main

'''
Sorted character array
input: geeksforgeeks
output: eeeefggkkorss
'''

def counting(arr):
    carr = [0] * 100
    for v in arr:
        carr[v] += 1

    ret = []
    for i in xrange(len(carr)):
        for j in xrange(carr[i]):
            ret.append(i)
    return ret

def ans(arr):
    arr = counting(arr)
    return ",".join( [str(x) for x in arr] )

if __name__ == "__main__":
    main.main(ans)
