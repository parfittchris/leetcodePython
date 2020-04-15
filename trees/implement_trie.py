# https: // leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isTerminal = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
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
            if not letter in root.children:
                return False
            else:
                root = root.children[letter]
        
        if root.isTerminal == True:
            return True
        else: 
            return False



    def startsWith(self, prefix):
        root = self.root

        for letter in prefix:
            if not letter in root.children:
                return False
            else:
                root = root.children[letter]

        return True


test = Trie()
test.insert('cat')
test.insert('bird')
test.insert('cart')
print(test.startsWith('b'))

