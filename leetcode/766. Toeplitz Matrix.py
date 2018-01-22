def ans1(matrix):
    '''
    zig-zag scan
    '''
    pass

def same(matrix, i, j):
    val = matrix[i][j]
    ni = i + 1
    nj = j + 1
    while ni < len(matrix) and nj < len(matrix[ni]):
        if matrix[ni][nj] != val:
            return False
        ni += 1
        nj += 1
    return True
        
def ans2(matrix):
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            if i != 0 and j != 0:
                continue
            if not same(matrix, i, j):
                return False
    return True

def ans4(matrix):
    '''
    check only next element
    '''
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            if i + 1 < len(matrix) and j + 1 < len(matrix[i]):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
    return True

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return ans4(matrix)
