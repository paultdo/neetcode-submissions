class PrefixTree:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        curr = self.head
        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            if curr.children[idx] == 0:
                curr.children[idx] = Node()
            curr = curr.children[idx]
            if i == len(word) - 1:
                curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] == 0:
                return False
            curr = curr.children[idx]
        
        if not curr.isEnd:
            return False
        
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            idx = ord(c) - ord('a')
            if curr.children[idx] == 0:
                return False
            curr = curr.children[idx]
        
        return True

class Node:
    def __init__(self):
        self.children = [0] * 26
        self.isEnd = False
        
        