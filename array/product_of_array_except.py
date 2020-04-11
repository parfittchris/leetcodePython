# https: // leetcode.com/problems/product-of-array-except-self/


def productExceptSelf(nums):
    final = []
    total = 1
    zero_count = 0

    for el in nums:
        if el == 0:
            zero_count += 1
        else:
            total *= el

    for el in nums:
        if zero_count == 0:
            new_value = total / el
        elif zero_count == 1 and el == 0:
            new_value = total
        else:
            new_value = 0
        
        final.append(int(new_value))

    return final




input = [1, 2, 3, 4]
input = [1,1,0]
# input = [0,0]


print(productExceptSelf(input))

