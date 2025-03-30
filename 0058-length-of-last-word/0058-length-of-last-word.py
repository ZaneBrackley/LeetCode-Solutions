class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        s.lstrip()
        print(s)

        i = 0
        for c in s:
            if (c != ' '):
                i += 1
            elif (c == ' ' and i == 0):
                continue
            elif (c == ' ' and i > 0):
                break
        
        return i