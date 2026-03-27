class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []

        current = 1
        i = 0
        while current <= n and i < len(target):
            result.append('Push')

            if target[i] == current:
                i+=1
            else:
                result.append('Pop')
            
            current += 1
        
        return result
        