
def bin_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if a[mid] == x:
            return mid
        elif a[mid] > x:
            return bin_search(arr, low, mid-1,x)
        else:
            return bin_search(arr, mid+1, high, x)

a = [9,3,7,4,6,0,5,2]
z = bin_search(a, 0, len(a), 6)
print(z)

