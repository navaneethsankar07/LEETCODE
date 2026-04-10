class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        
        self.root = TrieNode()
        
        for product in products:
            self.insert(product)
        
        return self.getSuggestions(searchWord)
    
    
    def insert(self, word):
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            
            node = node.children[ch]
            
            if len(node.suggestions) < 3:
                node.suggestions.append(word)
    
    
    def getSuggestions(self, searchWord):
        node = self.root
        result = []
        
        for ch in searchWord:
            if node and ch in node.children:
                node = node.children[ch]
                result.append(node.suggestions)
            else:
                node = None
                result.append([])
        
        return result