class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        length = len(title)
        for x in range(length):
            wordslen = len(words[x])
            if wordslen<=2:
                words[x] = words[x].lower()
            else:
                words[x] = words[x].capitalize()
        return " ".join(words)

                