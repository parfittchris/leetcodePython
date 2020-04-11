# https: // leetcode.com/problems/two-sum/

def twoSum(nums, target):
    remainders = {}

    for idx in range(len(nums)):
        difference = target - nums[idx]
        
        print(difference)
        print(remainders)
    
        if difference in remainders:
            return [remainders[difference], idx]
        else:
            remainders[nums[idx]] = idx
    
    return None

arr = [2, 7, 11, 15]
target = 9

print(twoSum(arr, target))
