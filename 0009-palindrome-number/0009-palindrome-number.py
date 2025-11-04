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
        oldX = x
        revX = 0
        while oldX != 0:
            num = oldX % 10
            oldX = oldX // 10
            revX = revX * 10 + num

        if revX == x:
            return True
        return False