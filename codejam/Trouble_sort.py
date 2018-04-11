
def trouble_sort(arr):
    swap_cnt = 1
    while swap_cnt != 0:
        swap_cnt = 0
        for i in xrange(len(arr) - 2):
            if arr[i] > arr[i + 2]:
                arr[i], arr[i + 2] = arr[i + 2], arr[i]
                swap_cnt += 1
    for i in xrange(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return str(i)
    return "OK"   

def main():
    t = int(raw_input())
    for i in xrange(t):
        n = int(raw_input())
        arr = list(map(int, raw_input().split()))
        print "Case #%d: %s"%(i+1, trouble_sort(arr))

if __name__ == "__main__":
    main()
