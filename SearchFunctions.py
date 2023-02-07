######################################
# Binary Search Algorithms(Iterative) taken from:
# url: https://www.geeksforgeeks.org/binary-search/
# on 01/27/2023
# License: Share-alike
# url: https://www.geeksforgeeks.org/copyright-information/?ref=footer#
# Changelog:
# - set the starting value of mid to zero
# - set mid as the return value
######################################



# Python3 code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1


def binarySearch_sub(arr, l, r, x):

    # allow mid from each prev loop to persist
    mid = 0
    while l <= r:

        mid = l + (r - l) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return mid

# end def binarySearch(arr, l, r, x):



if __name__ == "__main__":
    # Driver Code
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = binarySearch_sub(arr, 0, len(arr) - 1, x)

    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")
