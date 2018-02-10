#code

def max_sum_subarray(nums):
    if len(nums) == 0:
        return 0
    maxsum = nums[0]
    si, ei = 0, 0
    rsi, rei = 0, 0
    tsum = 0
    for i in range(len(nums)):
        tsum += nums[i]
        ei += 1
        if tsum > maxsum:
            maxsum = tsum
            rsi = si
            rei = ei
        if tsum < 0:
            tsum = 0
            si, ei = i, i
    return (rsi, rei, maxsum)

def max_sum_submatrix(matrix):
    ROW = len(matrix)
    COL = len(matrix[0])
    ret = [0, 0, 0, 0]
    maxsum = matrix[0][0]
    for ci in range(COL):
        tmp = [0] * ROW
        for cj in range(ci, COL):
            for i in range(len(matrix)):
                tmp[i] += matrix[i][cj]
            si, ei, tsum = max_sum_subarray(tmp)
            if tsum > maxsum:
                maxsum = tsum
                ret[0] = si
                ret[1] = ci
                ret[2] = ei
                ret[3] = cj
    #print(ret, maxsum)    
    print(maxsum)
                
t = int(input())
for i in range(t):
    row, col = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    matrix = []
    for j in range(row):
        matrix.append(nums[j * col: j * col + col])
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print (matrix[i][j], end="\t")
        print("\n")
    '''
    max_sum_submatrix(matrix)
