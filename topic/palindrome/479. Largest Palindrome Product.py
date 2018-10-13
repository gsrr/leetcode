'''
[Mathematic]

I used the following approach. Let's denote the biggest palindrome product as palindrome = M * L. For N > 1 this palidrome has even number of digits and it can be represented as the sum:
palindrome = upper * 10^N + lower
We can expect that M and L are close to 10^N and we can represent them as M = 10^N - i, L = 10^N - j and hence
palindrome = (10^N - i) * (10^N - j) = 10^N * (10^N - (i + j)) + i * j
If we assume that i * j < 10^N (this assumption turned out to be true for N > 1) we can represent upper and lower in the following way:
upper = 10^N - (i + j)
lower = i * j
This is the system of equations which can be solved if we know upper and lower. Let's denote sum of i and j as a = i + j. It can be calculated as a = 10^N - upper. Because j = a - i equation for lower can be rewritten as
lower = a * i - i * i
This is a quadratic equation which can be solved using standard methods from textbooks.


'''



def match(pa, n):
    
    while low * low <= pa:
        if pa % low == 0:
            #print pa, low, pa/low
            v2 = pa/low
            if len(str(v2)) == n:
                return True
        low += 1
    return False

def inverse(num):
    tmp = 0
    while num != 0:
        tmp = tmp * 10 + num % 10
        num = num / 10
    return tmp

def ans(n):
    if n == 1:
        return 9 % 1337
    
    if n == 2:
        return 9009 % 1337
    
    up = pow(10, n) - 1
    low = pow(10, n - 1)
    for i in xrange(up, -1, -1):
        #si = str(i)
        #pa = int(si + si[::-1])
        pa = i * (10 ** n) + inverse(i)
        for j in xrange(up, low, -1):
            if pa / j > up:
                break
            if pa % j == 0:
                return pa % 1337
    return 0
    
class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        return ans(n)




print ans(3)
print ans(5)
print ans(8)
