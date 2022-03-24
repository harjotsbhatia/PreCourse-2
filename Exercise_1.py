# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):
    # write your code here
    # while lower pointer is less than or equal to higher pointer
    while l <= r:
      # finding mid point
        mid = (l + r+1) // 2
        # if mid point is our solution return it.
        if arr[mid] == x:
            return mid
        # if mid point is bigger than we will search first half 
        elif arr[mid] < x:
            l = mid + 1
        # if mid point is smaller than we will search second half     
        else:
            r = mid - 1
            
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 2

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
