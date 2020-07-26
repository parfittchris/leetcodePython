# https: // leetcode.com/problems/first-bad-version/
def firstBadVersion(n):
    low = 1
    high = n

    while low < high:
        mid = ((high + low) // 2)
    
        if not isBadVersion(mid) and isBadVersion(mid + 1):
            return mid + 1
        elif isBadVersion(mid):
            high = mid - 1
        else:
            low = mid + 1
    
    return mid



def isBadVersion(idx):
    return arr[idx]


arr = [False, True, True, True, True]
print(firstBadVersion(len(arr)))



       
