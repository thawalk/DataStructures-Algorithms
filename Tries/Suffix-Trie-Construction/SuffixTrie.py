class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # Time Complexity = O(n^2), where n is the number of total string | Space Complexity = O(n^2)
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.addToTrie(i, string)

    def addToTrie(self, startIdx, string):
        node = self.root
        for j in range(startIdx, len(string)):
            if string[j] not in node:
                node[string[j]] = {}
            node = node[string[j]]
        node[self.endSymbol] = True

    # Time Complexity = O(m), where m is the number of characters in the input string that needs to be checked | O(1)
    def contains(self, string):
        node = self.root
        for char in string:
            if char not in node:
                return False
            node = node[char]
        return self.endSymbol in node
        # return node[self.endSymbol] == True
