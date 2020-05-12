# https: // leetcode.com/problems/group-anagrams/


class Solution(object):
    def groupAnagrams(self, strs):
        results = []

        while len(strs):
            current_results = []
            current_word = strs.pop(0)
            current_results.append(current_word)
            idx = 0
            
            while idx < len(strs):
                if self.isAnagram(current_word, strs[idx]):
                    new_word = strs.pop(idx)
                    current_results.append(new_word)
                else:
                    idx += 1

            results.append(current_results)
        
        return results

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


                

input = ["eat", "tea", "tan", "ate", "nat", "bat", "toe"]

# Output:
# [
#     ["ate", "eat", "tea"],
#     ["nat", "tan"],
#     ["bat"]
# ]

test = Solution()
print(test.groupAnagrams(input))