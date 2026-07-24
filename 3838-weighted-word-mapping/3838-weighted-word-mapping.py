class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for x in words:
            total = 0
            for y in x:
                total += weights[ord(y)-97]
            ans.append(total)
        
        
        return ''.join([chr(122-x%26) for x in ans])