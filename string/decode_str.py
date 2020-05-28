class Solution:
    def decodeString(self, s: str) -> str:
        mults = []
        starts = []
        temps = [""]
        counter = 0

        ints = list('1234567890')

        i = 0

        res = ""
        temp = ""

        while i < len(s):
            if s[i] in ints:
                mults.append(int(s[i]))
            elif s[i] == '[':
                counter += 1
                temps.append('')
                k = i
                while (s[k] == '['):
                    k += 1

                starts.append(k + 1)
            elif s[i] == ']':
                currentStart = starts.pop()
                sub = s[currentStart:i]
                num = mults.pop()
                temp = num * sub
                temps[counter] = temp
                print(temps)
            
            i += 1
        
        
        return "".join(temps)

            


                
        




test = Solution()

s = "3[a]2[bc]"
# return "aaabcbc".
s = "3[a2[c]]"
# return "accaccacc".
# s = "2[abc]3[cd]ef"
# return "abcabccdcdcdef".


print(test.decodeString(s))
