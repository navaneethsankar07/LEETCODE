class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0
        for x in events:
            if x == 'W':
                counter += 1
                if counter == 10:
                    break
            elif x == 'WD' or x == 'NB':
                score += 1
            
            else:
                score += int(x)

        return [score, counter]
            