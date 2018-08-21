



def gcd(a, b):
    if a == 0:
        return b 
    return gcd(b%a, a)    

def lcm(a, b):
    return (a * b) / gcd(a, b) 

if __name__ == "__main__":
    print gcd(2, 4)
    print gcd(1, 3)
    print gcd(4, 12)
    print gcd(10, 12)

    print
    print lcm(2, 4)
    print lcm(1, 3)
    print lcm(4, 12)
    print lcm(10, 12)
