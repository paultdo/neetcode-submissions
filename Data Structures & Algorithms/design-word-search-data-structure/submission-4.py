class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        index = 0
        return self.dfs(word, index, self.root)

    def dfs(self, word, index, root):
        curr = root
        wrd = word[index:]
        for i in range(len(wrd)):
            c = wrd[i]
            if c == ".":
                for child in curr.children.values():
                    res = self.dfs(word, index + i + 1, child)
                    if res:
                        return True
                
                return False

            else:
                if c not in curr.children:
                    return False
                curr = curr.children[c]
        
        return curr.isEnd



class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
