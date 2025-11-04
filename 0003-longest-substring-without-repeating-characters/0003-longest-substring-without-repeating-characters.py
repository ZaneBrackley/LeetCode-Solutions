class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        substr = []

        for ch in s:
            if ch not in substr:
                substr.append(ch)
            else:
                length = max(length, len(substr))
                k = substr.index(ch)
                substr = substr[k+1:]
                substr.append(ch)
        
        length = max(length, len(substr))
        return length