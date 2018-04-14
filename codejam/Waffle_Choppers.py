
def waffle_util(matrix, h, v, sumc):
    if h == 0 and v == 0:
        return sumc

    if (h + 1) >= len(matrix):
        return 0

    if len(matrix) != 0 and (v + 1) > len(matrix[0]):
        return 0

    if sumc % ((h + 1) * (v + 1)) != 0:
        return 0

def transpose(matrix):
    rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return rez
    
'''
def waffle(matrix, h, v):
    sumc = get_num_chocolate(matrix)
    if h == 0 and v == 0:
        return sumc

    if (h + 1) >= len(matrix):
        return 0

    if len(matrix) != 0 and (v + 1) > len(matrix[0]):
        return 0

    if sumc % ((h + 1) * (v + 1)) != 0:
        return 0

    ret = 0
    if h != 0:
        for i in xrange(1, len(matrix)):
            ret += waffle_util(matrix[1:len(matrix)], h - 1, v) 
    else:
        transpose(matrix)
        for i in xrange(1, len(matrix)):
            ret += waffle_util(matrix[1:len(matrix)], v - 1, h) 
        transpose(matrix)
    return ret
'''

import itertools

def get_num_chocolate(matrix):
    cnt = 0
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            if matrix[i][j] == "@":
                cnt += 1
    return cnt

def check_val(matrix, p1, p2, hist):
    if hist.has_key((p1, p2)):
        return hist[(p1, p2)]
    cnt = 0
    for i in xrange(p1[0], p2[0]):
        for j in xrange(p1[1], p2[1]):
            if matrix[i][j] == "@":
                cnt += 1
    hist[(p1, p2)] = cnt
    return cnt

def check_matrix(matrix, hcomb, vcomb, tval, hist):
    hcomb = hcomb + (len(matrix),)
    vcomb = vcomb + (len(matrix[0]),)
    #print check_matrix, hcomb, vcomb
    sh = 0
    sv = 0
    for eh in hcomb:
        p1 = (sh, sv)
        for ev in vcomb:
            p2 = (eh, ev)
            cnt = check_val(matrix, p1, p2, hist) 
            if cnt != tval:
                return False
            sv = ev
            p1 = (sh, sv)
        sh = eh
        sv = 0
    return True

def waffle(matrix, r, c, h, v):
    '''
    Brute method
    '''
    sumc = get_num_chocolate(matrix)
    print sumc
    if sumc % ((h + 1) * (v + 1)) != 0:
        return "IMPOSSIBLE"
    
    if sumc == 0:
        return "POSSIBLE"
    tval = sumc / ((h + 1) * (v + 1))
    hset = range(r + 1)[1:-1]
    vset = range(c + 1)[1:-1]
    hist = {}
    for hcomb in itertools.combinations(hset, h):
        for vcomb in itertools.combinations(vset, v):
            if check_matrix(matrix, hcomb, vcomb, tval, hist) == True:
                return "POSSIBLE"
    return "IMPOSSIBLE"

def check_val_row(matrix, tval):
    cnt = 0
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            if matrix[i][j] == "@":
                cnt += 1
        if cnt == tval:
            cnt = 0
        elif cnt < tval:
            pass
        else:
            return False
    return cnt == 0

def waffle3(matrix, r, c, h, v):
    '''
    Greedy method
    Time complexity : n * n + n * n + n * n, O(n^2)
    Space complexity : O(n^2) for transpose matrix
    '''
    sumc = get_num_chocolate(matrix)
    if sumc % ((h + 1) * (v + 1)) != 0:
        return "IMPOSSIBLE"
    
    if sumc == 0:
        return "POSSIBLE"
    
    if sumc == (r * c) and sumc == ((h + 1) == (v + 1)):
        return "POSSIBLE"

    h_tval = sumc / (h + 1)
    if check_val_row(matrix, h_tval) == False:
        return "IMPOSSIBLE"
    tmatrix = transpose(matrix)

    if tmatrix == matrix:
        return "IMPOSSIBLE"
    v_tval = sumc / (v + 1)
    if check_val_row(tmatrix, v_tval) == False:
        return "IMPOSSIBLE"
    return "POSSIBLE"

def main():
    t = int(raw_input())
    for i in xrange(t):
        matrix = []
        r, c, h, v = map(int, raw_input().split())
        #print r, c, h, v
        matrix = []
        for j in xrange(r):
            matrix.append(list(raw_input()))
        print "Case #%d: %s"%(i+1, waffle3(matrix, r, c, h, v))

if __name__ == "__main__":
    main()
