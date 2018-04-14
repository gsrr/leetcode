import sys
import random



def waffle():
    f = "input.Waffle_Choppers.2"
    with open(f, "w") as fw:
        fw.write("1\n")
        fw.write("100 100 49 49\n")
        cnt = 2500
        for i in xrange(100):
            line = []
            for j in xrange(100):
                val = random.randint(0, 10)
                if val % 2 == 0 and cnt != 0:
                    line.append("@")
                    cnt -= 1
                else:
                    line.append(".")
            print line
            fw.write("".join(line) + "\n")


def main():
    print sys.argv
    func = getattr(sys.modules[__name__], sys.argv[1])
    func()


if __name__ == "__main__":
    main()
