# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.


def valid_pal(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        else:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

    return True

string = "A aman, a plan, a canal: Panama"
# Output: true

print(valid_pal(string))