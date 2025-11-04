class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        x = str(x)
        n = len(x)
        left, right = 0, n-1
        while left <= right:
            if x[left] == x[right]:
                left += 1
                right -= 1
            else:
                return False
        return True