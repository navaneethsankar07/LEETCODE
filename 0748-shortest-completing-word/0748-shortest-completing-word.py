from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = ''
        for x in licensePlate:
            if x.isalpha():
                letters += x.lower()

        freq = Counter(letters)
        answer = ''

        for word in words:
            word_freq = Counter(word.lower())
            valid = True
            for letter in freq:
                if word_freq[letter] < freq[letter]:
                    valid = False
                    break
            
            if valid:
                if answer == '' or len(word) < len(answer):
                    answer = word
            

        return answer