import sys


def print_err(msg):
    print >> sys.stderr, msg

def print_out(x, y):
    print x, y
    sys.stdout.flush()

def isfull(x, y, farm):
    direct = [
        [0, 0],
        [0, 1],
        [0, -1],
        [-1, 0],
        [1, 0],
        [1, 1],
        [1, -1],
        [-1, -1],
        [-1, 1],
    ]
    for v1, v2 in direct:
        nx = x + v1
        ny = y + v2
        if farm.has_key((nx, ny)) == False:
            return False
    return True


def main():
    t = int(raw_input())
    for i in xrange(t):
        A = int(raw_input())
        #print_err("(t, A) = (%d, %d)" %(t, A))
        farm = {}
        x_base = 500
        y_base = 500
        x = x_base
        y = y_base
        while x > 0 and y > 0:
            print_out(x_base, y_base)
            x, y = list(map(int, raw_input().split()))
            #print_err("(x, y) = (%d, %d)"%(x, y))
            farm[(x, y)] = True
            if len(farm.keys()) == 9:
                y_base += 3
                farm = {}
        if x == -1 and y == -1:
            break

if __name__ == "__main__":
    main()
