def mergeSorted(arr1, arr2, m, n):
    idx = len(arr1) - 1

    while idx >= 0:
        if m == 0:
            arr1[idx] = arr2[n - 1]
            n -= 1
        elif n == 0:
            arr1[idx] = arr1[m-1]
            m -= 1
        elif arr1[m - 1] > arr2[n - 1]:
            arr1[idx] = arr1[m-1]
            m -= 1
        else:
            arr1[idx] = arr2[n-1]
            n -= 1
        
        idx -= 1
        

    return arr1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

print(mergeSorted(nums1, nums2, m, n))
