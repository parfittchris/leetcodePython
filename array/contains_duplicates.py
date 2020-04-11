# https: // leetcode.com/problems/contains-duplicate/
def containsDuplicate(nums):
    duplicates = {}

    for el in nums:
        if el in duplicates:
            return True
        duplicates[el] = True
    
    return False

input = [1, 2, 3]

print(containsDuplicate(input))