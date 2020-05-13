class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split(' ')

        for i in range(len(split)):
            split[i] = self.reverseOne(split[i])
        
        return " ".join(split)

    def reverseOne(self, word: str) -> str:
        i = 0
        j = len(word) - 1

        split_word = list(word)

        while i < j:
            [split_word[i], split_word[j]] = [split_word[j], split_word[i]]

            i += 1
            j -= 1
        
        return "".join(split_word)



test = Solution()
word = 'testing is the universe'
print(test.reverseWords(word))

