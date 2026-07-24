class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for x in words:
            total = 0
            for y in x:
                total += weights[ord(y)-97]
            ans.append(chr(122-total%26))
        
        
        return ''.join(ans)