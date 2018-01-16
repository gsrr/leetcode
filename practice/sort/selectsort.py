
def ans1(arr):
    for i in xrange(len(arr)):
        for j in xrange(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]


class Solution:
    def selectSort(self, arr):
        #ans(arr, 0, len(arr))
        #ans2(arr, 0, len(arr))
        print ans1(arr)

def main():
    sol = Solution()
    with open("input", "r") as fr:
        num = map(int, fr.readline().strip())[0]
        for i in xrange(num):
            arr = map(int, fr.readline().strip().split())
            sol.selectSort(arr)
            print " ".join(map(str, arr))


if __name__ == "__main__":
    main()
