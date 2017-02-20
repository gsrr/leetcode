# yield can not be used in recursive function.

answer = 0
def perm(nums, k = 0):
    global answer
    if k == len(nums): # last item
        answer += 1

    for i in xrange(k, len(nums)):
        if (k + 1) % nums[i] == 0 or nums[i] % (k + 1) == 0:
            nums[k], nums[i] = nums[i], nums[k]
            perm(nums, k + 1)
            nums[k], nums[i] = nums[i], nums[k]

def main():
    global answer
    answer = 0
    perm(range(1, 5), 0)
    return answer

if __name__ == "__main__":
    print main()
