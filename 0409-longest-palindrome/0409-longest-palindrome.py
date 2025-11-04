class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        length = 0
        removed = 0
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        print(freq)
        for key, value in freq.items():
            if value % 2 != 0:
                freq[key] -= 1
                removed = 1
            length += (freq[key])
        return length + removed