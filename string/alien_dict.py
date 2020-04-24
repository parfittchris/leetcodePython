# https: // leetcode.com/problems/verifying-an-alien-dictionary/


def isAlienSorted(self, words, order):
    for i in range(len(words) - 1):
        current = words[i]
        next_word = words[i + 1]

        idx = 0

        while idx < len(current):
            left = current[idx] if idx < len(current) else None
            right = next_word[idx] if idx < len(next_word) else None

            if not right:
                return False

            leftIdx = order.index(left)
            rightIdx = order.index(right)

            if leftIdx == rightIdx:
                idx += 1
            elif leftIdx < rightIdx:
                break
            else:
                return False

    return True
