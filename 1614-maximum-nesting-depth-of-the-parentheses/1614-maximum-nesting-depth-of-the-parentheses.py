class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        maxDepth = 0

        for ch in s:
            if ch == "(":
                count += 1
                if count > maxDepth:
                    maxDepth = count
            elif ch == ")":
                count -= 1
            else:
                continue
        
        return maxDepth