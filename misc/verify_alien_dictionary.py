# https: // leetcode.com/problems/verifying-an-alien-dictionary/

def isAlienSorted(words, order: str) -> bool:
    pointer = 0

    while pointer < len(words) - 1:
        word1 = words[pointer]
        word2 = words[pointer + 1]
        i = 0

        while i < len(word1):
            idx1 = order.index(word1[i]) if i < len(word1) else None
            idx2 = order.index(word2[i]) if i < len(word2) else None

            if idx1 == None:
                break
            elif idx2 == None:
                return False
            else:
                if idx2 > idx1:
                    break
                elif idx1 > idx2:
                    return False
                else:
                    i += 1
        
        pointer += 1
    
    return True

words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"

print(isAlienSorted(words, order))
