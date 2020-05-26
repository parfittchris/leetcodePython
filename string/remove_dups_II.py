def removeDuplicates(s: str, k: int) -> str:
    found = True
    i = 0 

    while i < (len(s) - k):
        sub = s[i:i + k] 
        if verifyKs(sub, k):
            found = True
            s = s[:i] + s[i + k:]
            i = 0
        else: 
            i += 1
            

    return s


def verifyKs(string, l):
    if len(string) < l:
        return False

    idx = 0

    while l > 0 and idx < (len(string) - 1):
        if string[idx] == string[idx + 1]:
            idx += 1
        else:
            return False

    return True

                 

s = "deeedbbcccbdaa"
k = 3


print(removeDuplicates(s, k))
# print(verifyKs('eee', k))

