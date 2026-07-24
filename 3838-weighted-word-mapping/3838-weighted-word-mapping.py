class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for x in words:
            res = []
            for y in x:
                res.append(weights[ord(y)-97])
            ans.append(sum(res))
        
        
        return ''.join([chr(122-x%26) for x in ans])