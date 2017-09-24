def get_next_xy(x, y, direction, n, matrix):
    if direction == "right":
        if y + 1 < n and matrix[x][y + 1] == 0:
            return x, y + 1, direction
        else:
            return x + 1, y, "down"
    
    elif direction == "down":
        if x + 1 < n and matrix[x + 1][y] == 0:
            return x + 1, y, direction
        else:
            return x, y - 1, "left"
    elif direction == "left":
        if y - 1 >= 0 and matrix[x][y - 1] == 0:
            return x, y - 1, direction
        else:
            return x - 1, y, "up"
    elif direction == "up":
        if x - 1 >= 0 and matrix[x - 1][y] == 0:
            return x - 1, y, direction
        else:
            return x, y + 1, "right"
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for i in xrange(n)]
        print matrix
        cnt = 1
        tn = n * n
        x = 0
        y = 0
        direction = "right"
        while cnt <= tn:
            matrix[x][y] = cnt
            x, y, direction = get_next_xy(x, y, direction, n, matrix)
            cnt += 1
        return matrix
