# https: // leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        counter = {}

        for letter in s:
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1

        
        for letter in t:
            if letter in counter:
                counter[letter] -= 1
            else:
                return False
        

        for letter in counter:
            if counter[letter] != 0:
                return False
            

        return True

s = "anagram" 
t = "nagaram7"

test = Solution()
print(test.isAnagram(s, t))
