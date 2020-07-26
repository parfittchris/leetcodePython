def longestSub(s, k):
    current = ""

    for i in reversed(range(len(s))):
        for j in range(i+1):
            sub = s[j:i+1]
            if isValid(sub, k) and len(sub) > len(current):
                current = sub
            
    return current
    
def isValid(s, k):
    counter = {}

    for char in s:
        if not char in counter:
            counter[char] = 1
        else:
            counter[char] += 1
    
    for el in counter:
        if counter[el] < k:
            return False

    return True


s1 = 'aaabb'
print(longestSub(s1, 2))

