import main

def ans(arr, val):
    for i in xrange(len(arr)):
        if arr[i] == val:
            return str(i)

if __name__ == "__main__":
    main.main(ans)
