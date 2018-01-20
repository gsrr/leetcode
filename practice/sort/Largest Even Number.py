#code
import collections

def main():
    n = int(input())
    #print(n)
    for i in range(n):
        num = input()
        nlist = list(num)
        narr = [0] * 10
        for i in range(len(nlist)):
            narr[int(nlist[i])] += 1
        #print(narr)
        val = 0
        min_even = -1
        for i in range(10):
            if i % 2 == 0 and narr[i] != 0:
                min_even = i
                narr[i] -= 1
                break
        for i in range(10 - 1, -1, -1):
            while narr[i] != 0:
                val = val * 10 + i
                narr[i] -= 1
        if min_even != -1:
            val = val * 10 + min_even
        print(val)
if __name__ == "__main__":
    main()
