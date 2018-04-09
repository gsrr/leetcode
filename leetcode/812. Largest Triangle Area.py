def get_area(p1, p2, p3):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x3 = p3[0]
    y3 = p3[1]
    v1 = (x1 * y2 + x2 * y3 + x3 * y1)
    v2 = (y1 * x2 + y2 * x3 + y3 * x1)
    return abs((v1 - v2)) * 0.5


def recur_util(points, path):
    if len(path) == 3:
        return get_area(path[0], path[1], path[2])
    
    max_val = 0
    for i in xrange(len(points)):
        path.append(points[i])
        max_val = max(max_val, recur_util(points[i + 1:], path))
        path.pop()
    return max_val
    
def ans1(points):
    '''
    Recursive method
    Time Complexity : O(n^3)
    Space Complexity : O(3) and path for storing points, the number of function call is 3 at most.
    '''
    max_val = 0
    path = []
    for i in xrange(len(points)):
        path.append(points[i])
        max_val = max(max_val, recur_util(points[i + 1:], path))
        path.pop()
    return max_val
                      
def ans2(points):
    '''
    iterative method
    Time complexity : O(n^3)
    Space complexity : O(1), no stack for function call
    '''
    max_val = 0
    for i in xrange(len(points)):
        for j in xrange(i + 1, len(points)):
            for k in xrange(j + 1, len(points)):
                max_val = max(max_val, get_area(points[i], points[j], points[k]))
    return max_val

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        return ans1(points)

    def largestTriangleArea2(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        return ans2(points)

points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
s = Solution()
print s.largestTriangleArea(points)
print s.largestTriangleArea2(points)
