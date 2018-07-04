import collections

def transpose(matrix):
    return [list(x) for x in zip(*matrix)]

def ans(matrix):
    for i in xrange(len(matrix)):
        if matrix[i][0] == 0:
            #togg_row
            for j in xrange(len(matrix[i])):
                matrix[i][j] = 1 - matrix[i][j]
    
    #print matrix
    matrix = transpose(matrix)
    #print matrix
    for i in xrange(1, len(matrix)):
        ct = collections.Counter(matrix[i])
        if ct[0] > ct[1]:
            # togg_colume
            for j in xrange(len(matrix[i])):
                matrix[i][j] = 1 - matrix[i][j]
    #print matrix
    matrix = transpose(matrix)
    #print matrix
    ret = 0
    for i in xrange(len(matrix)):
        bstr = "".join([ str(x) for x in matrix[i] ])
        ret += int(bstr, 2)
    return ret

class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        return ans(A)
