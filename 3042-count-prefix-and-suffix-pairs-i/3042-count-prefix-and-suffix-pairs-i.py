class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1,str2):
            if str2.startswith(str1) and str2.endswith(str1):
                return True
            return False
        
        length = len(words)
        count = 0
        for x in range(length):
            for y in range(x+1,length):
                if isPrefixAndSuffix(words[x],words[y]):
                    count+=1
        return count