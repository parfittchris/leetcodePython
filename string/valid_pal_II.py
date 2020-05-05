# https: // leetcode.com/problems/valid-palindrome-ii/

def valid_pal_II(s):
    i = 0
    j = len(s) - 1
    count = 1

    while i < j:
        if s[i] != s[j]:
            newLeft = s[:i] + s[i + 1:]
            newRight = s[:j] + s[j + 1:]
            return isPal(newLeft) or isPal(newRight)
        
        i += 1
        j -= 1
    
    return True

        


def isPal(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        
        i += 1
        j -= 1
    
    return True

test = 'axbca'
print(valid_pal_II(test))
# print(isPal(test))
