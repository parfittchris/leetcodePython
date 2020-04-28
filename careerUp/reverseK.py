# reverse an array for k distance

def reverseK(arr,k):
    arr2 = arr[:k]

    i = 0
    j = len(arr2) - 1

    while (i < j):
        [arr2[i], arr2[j]] = [arr2[j], arr2[i]]
        i += 1
        j -= 1
    
    return arr2 + arr[k:]
    
    


arr = [2,3,1,5,4]
k = 3

print(reverseK(arr,k))