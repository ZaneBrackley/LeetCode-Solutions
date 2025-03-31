class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        justafied = []
        currentIndex, totalWords = 0, len(words)

        while currentIndex < totalWords:
            lineWords = []
            count = len(words[currentIndex])
            lineWords.append(words[currentIndex])
            currentIndex += 1

            while currentIndex < totalWords and count + 1 + len(words[currentIndex]) <= maxWidth:
                count += 1 + len(words[currentIndex])
                lineWords.append(words[currentIndex])
                currentIndex += 1
            
            if currentIndex == totalWords or len(lineWords) == 1:
                lineLeftJustafied = ' '.join(lineWords)
                spacesOnRight = ' ' * (maxWidth - len(lineLeftJustafied))
                justafied.append(lineLeftJustafied + spacesOnRight)
                continue

            totalSpaces = maxWidth - (count - len(lineWords) + 1)
            spaceWidth, extraSpaces = divmod(totalSpaces, len(lineWords) - 1)

            constructedLine = []
            for index, word in enumerate(lineWords[:-1]):
                constructedLine.append(word)
                constructedLine.append(' ' * (spaceWidth + (1 if index < extraSpaces else 0)))

            constructedLine.append(lineWords[-1])
            justafied.append(''.join(constructedLine))

        return justafied