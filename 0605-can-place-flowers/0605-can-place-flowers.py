class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        length = len(flowerbed)
        for x in range(length):
            if flowerbed[x] == 0 and (x == 0 or flowerbed[x-1] == 0) and (x == length - 1 or flowerbed[x+1] == 0):
                flowerbed[x] = 1
                n -= 1
                if n == 0:
                    return True
        
        return False