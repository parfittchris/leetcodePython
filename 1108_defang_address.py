# https://leetcode.com/problems/defanging-an-ip-address/
# Given a valid(IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".


def test(word):
    result = ""
    for i in range(len(word)):
        if word[i] == '.':
            result += '[.]'
        else:
            result += word[i]
    return result


print(test('cat....'))
