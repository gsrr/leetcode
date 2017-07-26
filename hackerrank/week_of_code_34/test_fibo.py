from math import sqrt
import sys

def fibo_math(n):
    c = (1 + sqrt(5)) ** n
    print c
    #return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fibo(n - 1) + fibo(n - 2)

if __name__ == "__main__":
    print fibo(int(sys.argv[1]))
