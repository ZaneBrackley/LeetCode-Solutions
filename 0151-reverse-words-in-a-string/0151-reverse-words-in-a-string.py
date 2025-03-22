class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        words = s.split()

        reversedWords = ""

        for word in reversed(words):
            reversedWords += word + " "

        reversedWords = reversedWords.strip()

        return reversedWords