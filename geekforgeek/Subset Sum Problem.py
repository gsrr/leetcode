#code

# Returns true if there is a subset 
# of set[] with sun equal to given sum
def isSubsetSum(st, n, sm) :
   
    # The value of subset[i][j] will be
    # true if there is a subset of 
    # set[0..j-1] with sum equal to i
    subset=[[True] * (sm+1)] * (n+1)
   
    # If sum is 0, then answer is true
    for i in range(0, n+1) :
        subset[i][0] = True
   
    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, sm + 1) :
        subset[0][i] = False
   
    # Fill the subset table in botton 
    # up manner
    for i in range(1, n+1) :
        for j in range(1, sm+1) :
            if(j < st[i-1]) :
                subset[i][j] = subset[i-1][j]
            if (j >= st[i-1]) :
                subset[i][j] = subset[i-1][j] or subset[i - 1][j-st[i-1]]
   
    """uncomment this code to print table
    for i in range(0,n+1) :
        for j in range(0,sm+1) :
            print(subset[i][j],end="")
    print(" ")"""
   
    return subset[n][sm];

def ans(arr):
    if sum(arr) % 2 != 0:
        return "NO"
    tval = sum(arr) // 2 
    dp = {}
    dp[0] = True
    for i in range(len(arr)):
        keys = list(dp.keys())
        for k in keys:
            dp[k + arr[i]] = True
            if tval in dp:
                return "YES"
    return "NO"

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print (ans(arr))
