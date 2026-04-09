class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            
            node = node.children[ch]
        
        node.isEnd = True

    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.root)

    
    def _dfs(self, word, index, node):

        for i in range(index, len(word)):
            ch = word[i]

            if ch == '.':
                for child in node.children.values():
                    if self._dfs(word,i+1, child):
                        return True
                return False
            
            else:
                if ch not in node.children:
                    return False
                
                node = node.children[ch]
            
        return node.isEnd

