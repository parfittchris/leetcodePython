# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space(size that is equal to m + n) to hold additional elements from nums2.


def mergeSorted(arr1, arr2, m, n):
    i = len(arr1) - 1

    while i >= 0:
        if m == 0:
            next_val = arr2[n - 1]
            n -= 1
        elif n == 0:          
            next_val = arr1[m - 1]
            m -= 1
        else:
            if arr1[m - 1] > arr2[n - 1]:
                next_val = arr1[m - 1]
                m -= 1
            else:
                next_val = arr2[n - 1]
                n -= 1
            
        arr1[i] = next_val
        i -= 1
    
    return arr1


nums1 = [-1, -1, 0, 0, 0, 0]

m = 4
nums2 = [-1, 0]

n = 2

print(mergeSorted(nums1, nums2, m, n))
# Output: [1, 2, 2, 3, 5, 6]
