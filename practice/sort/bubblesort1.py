

def ans1(arr):
    for i in xrange(len(arr) - 1, 0, -1):
        for j in xrange(1, i + 1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

def ans2(arr):
    for i in xrange(len(arr)):
        for j in xrange(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

class Solution:
    def bubbleSort(self, arr):
        #print ans1(arr)
        print ans2(arr)

def main():
    sol = Solution()
    with open("input", "r") as fr:
        num = map(int, fr.readline().strip())[0]
        for i in xrange(num):
            arr = map(int, fr.readline().strip().split())
            sol.bubbleSort(arr)
            print " ".join(map(str, arr))


if __name__ == "__main__":
    main()
