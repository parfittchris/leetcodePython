class Solution:
    def removeDuplicates(self, S: str) -> str:
        pair_found = True

        while pair_found:
            pair_found = False
            for i in range(len(S) - 1):
                if S[i] == S[i + 1]:
                    S = S[:i] + S[i + 2:]
                    pair_found = True
                    break
        
        return S
            



test = Solution()
word = 'abbaca'
print(test.removeDuplicates(word))