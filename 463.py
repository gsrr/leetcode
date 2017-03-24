def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def ans(grid):
    ones = 0
    r = 0
    for i in xrange(len(grid)):
        for j in xrange(len(grid[i])):
            if grid[i][j] == 1:
                ones += 1
                for (x,y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if x < len(grid) and x > -1 and y < len(grid[i]) and y > -1 :
                        if grid[x][y] == 1:
                            r += 1
    return ones * 4 - r

cases = [
    [[[0,1,0,0],
         [1,1,1,0],
          [0,1,0,0],
           [1,1,0,0]]
        ]
]
test(cases,1)

