
def insert1(src, tgt, idx):
    val = src[idx]
    j = idx
    while j > 0 and val < tgt[j - 1]:
        tgt[j] = tgt[j - 1]
        j -= 1
    tgt[j] = val

def insert2(val, arr, i):
    j = i
    arr[j] = val
    while j > 0 and arr[j] < arr[j - 1]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1

def insert3(arr, i):
    val = arr[i]
    j = i
    while j > 0 and arr[j - 1] > val:
        arr[j] = arr[j - 1]
        j -= 1
    arr[j] = val

def ans(arr):
    for i in xrange(len(arr)):
        #insert1(arr, ret, i)
        #insert2(arr[i], ret, i)
        insert3(arr, i)
    return arr

class Solution:
    def insertionSort(self, arr):
        return ans(arr)

def main():
    sol = Solution()
    with open("input", "r") as fr:
        num = map(int, fr.readline().strip())[0]
        for i in xrange(num):
            arr = map(int, fr.readline().strip().split())
            ret = sol.insertionSort(arr)
            print " ".join(map(str, ret))


if __name__ == "__main__":
    main()
