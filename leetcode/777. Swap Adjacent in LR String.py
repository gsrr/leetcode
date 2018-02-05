def moveL(start, end):
    i = 0
    j = 0
    while i < len(start) and j < len(end):
        while i < len(start) and start[i] != "L":
            i += 1
        
        while j < len(end) and end[j] != "L":
            j += 1
        
        if j == len(end):
            break
        
        if i == len(start):
            break
            
        while i > j and start[i - 1] == "X":
            start[i] = start[i - 1]
            i -= 1
        start[i] = 'L'
        i += 1
        j += 1

def moveR(start, end):
    i = len(start) - 1
    j = len(end) - 1
    while i > -1 and j > -1:
        while i > -1 and start[i] != "R":
            i -= 1
        
        while  j > -1 and end[j] != "R":
            j -= 1
        
        if i == -1 or j == -1:
            break
        while i < j and start[i + 1] == "X":
            start[i] = start[i + 1]
            i += 1
        start[i] = 'R'
        i -= 1
        j -= 1
        
def ans(start, end):
    if len(start) != len(end):
        return False
    
    moveL(start, end)
    moveR(start, end)
    
    return "".join(start) == "".join(end)

class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        return ans(list(start), list(end))
        
