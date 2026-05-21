class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        result = set()

        for x in bulbs:
            if x in result:
                result.remove(x)
            else:
                result.add(x)
        
        result = sorted(result)
        return result