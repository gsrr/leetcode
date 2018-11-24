#code

def is_palindrome1(s):
    return s == s[::-1]

def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True
    
def ans(s):
    if is_palindrome(s):
        return "Yes"
    else:
        return "No"
    

t = int(input())
for _ in range(t):
    ls = int(input())
    s = input()
    print(ans(s))
