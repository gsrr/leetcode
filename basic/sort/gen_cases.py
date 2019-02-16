import random
import sys


def gen_sort(num):
    with open("cases", "w") as fw:
        for i in xrange(num):
            arr = [ x for x in random.sample(range(30), 10)]
            fw.write("[[%s]]"%(",".join([ str(x) for x in arr])))
            fw.write("\n")
            arr.sort()
            fw.write(",".join([str(x) for x in arr]))
            fw.write("\n")

def gen_search(num):
    with open("cases", "w") as fw:
        for i in xrange(num):
            arr = [ str(x) for x in random.sample(range(1000), 30)]
            pos = random.randint(0, 30)
            fw.write("[[%s], %s]"%(",".join(arr), arr[pos]))
            fw.write("\n")
            fw.write("%d\n"%(pos))

def main():
    func = getattr(sys.modules[__name__], sys.argv[1])
    func(10)

if __name__ == "__main__":
    main()
