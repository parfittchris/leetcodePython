# https: // leetcode.com/problems/first-bad-version/
def firstBadVersion(n):
    high = len(n) - 1
    low = 0
    count = 0
    resultIdx = None

    while low < high:
        if n[low] == 'bad':
            resultIdx = low
            break

        mid = (high - low) / 2

        if n[mid] == 'Good':
            low = mid + 1
            count += 1
        else:
            high = mid - 1
            count += 1
            
    return count



arr = ['bad', 'Good', 'Good', 'bad', 'bad']
print(firstBadVersion(arr))


       
