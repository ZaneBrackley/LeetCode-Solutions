class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        ws = s.split()

        if len(ws) != len(pattern):
            return False

        letterWord = {}
        wordLetter = {}

        for letter, word in zip(pattern, ws):
            if (letter in letterWord and letterWord[letter] != word) or (word in wordLetter and wordLetter[word] != letter):
                return False
            
            letterWord[letter] = word
            wordLetter[word] = letter

        return True
        
        
        