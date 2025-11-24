class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        prev = ''
        for x in words:
            current_sorted = sorted(x)
            if prev != current_sorted:
                result.append(x)
                prev = current_sorted
        return result
       