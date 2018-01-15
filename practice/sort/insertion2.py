def insert1(arr, i):
    val = arr[i]
    j = i
    while j > 0 and arr[j - 1] > val:
        arr[j] = arr[j - 1]
        j -= 1
    arr[j] = val

def ans1(arr):
    for i in xrange(len(arr)):
        insert1(arr, i)

class Solution:
    def insertionSort(self, arr):
        #return ans(arr)
        return ans2(arr)

def main():
    sol = Solution()
    with open("input", "r") as fr:
        num = map(int, fr.readline().strip())[0]
        for i in xrange(num):
            arr = map(int, fr.readline().strip().split())
            ret = sol.insertionSort(arr)
            print " ".join(map(str, arr))


if __name__ == "__main__":
    main()
