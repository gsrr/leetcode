class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = range(1, n+1)
        f3 = 0
        b5 = 0
        fb15 = 0
        for i in range(1, n+1):
            if i - 15 == fb15 :
                ret[i-1] = "FizzBuzz"
                fb15 = i
                b5 = i
                f3 = i
            elif i - 5 == b5:
                ret[i-1] = "Buzz"
                b5 = i
            elif i - 3 == f3:
                ret[i-1] = "Fizz"
                f3 = i
            else:
                ret[i-1] = str(i)
        return ret
