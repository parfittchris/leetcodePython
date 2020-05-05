# https: // leetcode.com/problems/intersection-of-two-arrays/

def intersect(arr1, arr2):
    return list(set(arr1) & set(arr2))


arr1 = [4, 9, 5]
arr2 = [9, 4, 9, 8, 4]


print(intersect(arr1, arr2))
