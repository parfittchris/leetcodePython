# https: // leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == " ":
            return 1

        longest = 0
        start = 0

        while start < len(s):
            seen = {}
            current = 0

            for letter in s[start:]:
                if letter in seen:
                    break
                else:
                    seen[letter] = True
                    current += 1

            longest = max(longest, current)
            start += 1

        return longest

input = "c"

test = Solution()
print(test.lengthOfLongestSubstring(input))

