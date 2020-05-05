# https: // leetcode.com/problems/next-permutation/submissions/

def nextPerm(arr):
    pivot = None
    i = len(arr) - 1
    j = len(arr) - 1
    
    while i >= 0:
        if i == 0:
            return sorted(arr)
        elif arr[i] > arr[i - 1]:
            pivot = i - 1
            break
        else:
            i -= 1
    
    while j >= 0:
        if arr[j] > arr[pivot]:
            [arr[pivot], arr[j]] = [arr[j], arr[pivot]]
            return arr[:j + 1] + sorted(arr[j + 1:])
        
        j -= 1



test = [1,2,3]

test = [5,7,3, 2, 3, 1, 5, 4, 3]
# 
print(nextPerm(test))

