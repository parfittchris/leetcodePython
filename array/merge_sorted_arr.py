# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space(size that is equal to m + n) to hold additional elements from nums2.


def mergeSorted(arr1, arr2, m, n):
    # set pointer to length of arr1 - 1
    pointer = len(arr1) - 1

    # while loop that moves pointer backwards. 
    while pointer >= 0:
        nextVal = None

    # fill current idx of arr1 with the greater of arr1[m]/arr2[n]
    # decrement m/n depending on whatever is used
    # if m or n is 0 choose other
        if m == 0:
            nextVal = arr2[n - 1]
            n -= 1
        elif n == 0:
            nextVal = arr1[m - 1]
            m -= 1
        elif arr2[n - 1] > arr1[m - 1]:
            nextVal = arr2[n - 1]
            n -= 1
        else:
            nextVal = arr1[m - 1]
            m -= 1
        

        arr1[pointer] = nextVal
    # decrement pointer
        pointer -= 1
        
    # return arr1
    return arr1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


print(mergeSorted(nums1, nums2, m, n))
# Output: [1, 2, 2, 3, 5, 6]
