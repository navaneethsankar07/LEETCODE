class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for x in image:
            x.reverse()
            for y in range(len(x)):
                x[y] ^= 1

        return image