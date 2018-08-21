


def bin_search_right(arr, val):
    s = 0
    e = len(arr)
    while s < e:
        mid = (s + e) / 2
        if arr[mid] < val:
            s = mid + 1
        elif arr[mid] > val:
            e = mid
        elif arr[mid] == val:
            # assign to s or assign to e?
            # assign to s due to go to right side.
            s = mid + 1
    return s


def bin_search_left(arr, val):
    s = 0
    e = len(arr)
    while s < e:
        mid = (s + e) / 2
        if arr[mid] < val:
            s = mid + 1
        elif arr[mid] > val:
            e = mid
        elif arr[mid] == val:
            # assign to s or assign to e?
            # assign to e due to go to left side.
            e = mid
    return s

def ans(arr):
    print bin_search_left(arr, 2) # index = 1
    print bin_search_right(arr, 2) - 1 # index = 6

def main():
    arr = [1, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ans(arr)

if __name__ == "__main__":
    main()
