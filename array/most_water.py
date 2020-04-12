# https: // leetcode.com/problems/container-with-most-water/


def maxArea(height):
    print(height)

    max_water = 0

    left = 0
    right = len(height) - 1

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, area)

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return max_water



input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(input))
