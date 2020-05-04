class TrieNode:
    def __init__(self):
        self.children = {}
        self.isTerminal = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        root = self.root

        for letter in word:
            if letter in root.children:
                root = root.children[letter]
            else:
                root.children[letter] = TrieNode()
                root = root.children[letter]
        
        root.isTerminal = True

    def search(self, word):
        root = self.root

        for letter in word:
            if letter not in root.children:
                return False
            else:
                root = root.children[letter]
        
        return root.isTerminal

test = WordDictionary()
test.addWord('cats')
test.addWord('dog')


print(test.search('dog'))
print(test.search('cat'))
