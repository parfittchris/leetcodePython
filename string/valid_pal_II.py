# https: // leetcode.com/problems/valid-palindrome-ii/

def valid_pal_II(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
           str1 = s[:i] + s[i + 1:]
           str2 = s[:j] + s[j+1:]
           print(str1, str2)
           return isPal(str1) or isPal(str2)
    
    return True


def isPal(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    
    return True


test = 'axdxda'
print(valid_pal_II(test))
# print(isPal(test))
