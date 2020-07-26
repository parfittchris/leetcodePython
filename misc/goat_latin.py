def toGoatLatin(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    split = s.split(" ")
    new_split = []

    i = 0

    while i < len(split):
        word = split[i]

        if word[0].lower() in vowels:
            new_word = word + 'ma'
        else:
            new_word = word[1:] + word[0] + 'ma'

        new_word = new_word + 'a' * (i + 1)
        new_split.append(new_word)
        i += 1

    
    return " ".join(new_split)

s = "I speak Goat Latin"
print(toGoatLatin(s))
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
