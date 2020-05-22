class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        counter = {}

        for el in nums:
            if el in counter:
                counter[el] = 0
            else:
                counter[el] = 1

        for el in counter:
            if counter[el] == 1:
                return el
