
def ans1(A, L, R):
    cnt = 0
    for i in xrange(len(A)):
        max_val = A[i]
        if max_val > R:
            continue
        if max_val >= L:
            cnt += 1
        j = i + 1
        while j < len(A):
            if max_val < A[j]:
                max_val = A[j]
            if max_val > R:
                break
            if max_val >= L:
                cnt += 1
            j += 1
    return cnt

A = [2, 1, 4, 3]
L = 2
R = 3
print ans1(A, L, R)

A = [73,55,36,5,55,14,9,7,72,52]
L = 32
R = 69
print ans1(A, L, R)
