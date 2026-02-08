class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        freq = dict(enumerate(list1))
        min_index = float('inf')
        min_word = []
        for i,x in enumerate(list2):
            if x in freq.values():
                key = next(k for k, v in freq.items() if v == x)
                print(key ,i )
                if (i+key)< min_index:
                    min_index = i+key
                    min_word = [x]
                elif(i+key)==min_index:
                    min_index = i+key
                    min_word.append(x)

        return min_word
