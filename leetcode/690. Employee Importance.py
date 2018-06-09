"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

def ans(emps, id):
    dic = {}
    for i in xrange(len(emps)):
        e = emps[i]
        dic[e.id] = [e.importance, e.subordinates]
    
    hist = {}
    gval = 0
    q = [id]
    while len(q) != 0:
        uid = q.pop(0)
        if hist.has_key(uid) == True:
            continue
        gval += dic[uid][0]
        hist[uid] = True
        for v in dic[uid][1]:
            q.append(v)
    return gval

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        return ans(employees, id)
