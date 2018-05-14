def ans(matrix):
    for i in xrange(len(matrix)):
        matrix[i] = matrix[i][::-1]
        for j in xrange(len(matrix[i])):
            matrix[i][j] = 1 - matrix[i][j]
    return matrix

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return ans(A)
