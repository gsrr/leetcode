def ans_2(asteroids):
    stack = []
    for i in xrange(len(asteroids)):
        stack.append(asteroids[i])
        while len(stack) > 1 and stack[-1] < 0 and stack[-1] * stack[-2] < 0:
            v1 = stack.pop()
            v2 = stack.pop()
            if abs(v1) > abs(v2):
                stack.append(v1)
            if abs(v1) < abs(v2):
                stack.append(v2)                 
    return stack

def ans_1(asteroids):
    stack = []
    for i in xrange(len(asteroids)):
        if len(stack) == 0 or asteroids[i] > 0:
            stack.append(asteroids[i])
        else:
            tval = asteroids[i]
            all_dead = False
            while len(stack) != 0:
                sval = stack[-1]
                if sval * tval > 0:
                    stack.append(tval)
                    break
                else:
                    if abs(sval) == abs(tval):
                        stack.pop()
                        all_dead = True
                        break
                    elif abs(sval) > abs(tval):
                        break
                    else:
                        stack.pop()
            if len(stack) == 0 and all_dead == False:
                stack.append(tval)
                        
    return stack

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if len(asteroids) == 0:
            return []
        return ans_1(asteroids)
