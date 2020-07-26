# A password is considered strong if below conditions are all met:

# It has at least 6 characters and at most 20 characters.
# It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
# It must NOT contain three repeating characters in a row("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
# Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

# Insertion, deletion or replace of any one character are all considered as one change.

def strongPasswordChecker(s) -> int:
    count = 0
    upper = False
    lower = False
    num = False

    if len(s) < 6:
        count += (6 - len(s))
    
    if len(s) > 20:
        count += len(s) - 20

    i = 0

    while i < len(s) - 2:
        j = i + 1
        k = i + 2

        if s[i].isupper() or s[j].isupper() or s[k].isupper():
            upper = True
        
        if s[i].islower() or s[j].islower() or s[k].islower():
            lower = True

        if s[i].isdigit() or s[j].isdigit() or s[k].isdigit():
            num = True
        
        if s[i] == s[j] == s[k]:
            count += 1
            i += 3
        else:
            i += 1

    if upper == False:
        count += 1
    
    if lower == False:
        count += 1

    if num == False:
        count += 1

    return count


string = "aaaaaa"
print(strongPasswordChecker(string))