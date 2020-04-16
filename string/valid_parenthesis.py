# https: // leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if len(stack) == 0 or self.compare(stack.pop(len(stack) - 1), char) != True:
                    return False
        
        return len(stack) == 0
    
    def compare(self, left, right):
        if left == '(' and right == ')':
            return True
        elif left == '{' and right == '}':
            return True
        elif left == '[' and right == ']':
            return True
        else:
            return False
        

input = "{[]}"

test = Solution()
print(test.isValid(input))
