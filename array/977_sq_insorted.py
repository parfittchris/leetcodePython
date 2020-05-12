# https: // leetcode.com/problems/squares-of-a-sorted-array/


def squares(arr):
    return sorted(map(lambda x: x * x, arr))
  



arr = [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]

print(squares(arr))
