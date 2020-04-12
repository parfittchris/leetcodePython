# https: // leetcode.com/problems/3sum/
def threeSum(nums):
        results = []
        nums = sorted(nums)

        for i in range(0, len(nums)-2):
            if nums[i] > 0:
                return results
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while(j < k):
                temp = nums[i] + nums[j] + nums[k]
                if temp < 0:
                    j += 1
                elif temp > 0:
                    k -= 1
                else:
                    results.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1

        
        return results


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
