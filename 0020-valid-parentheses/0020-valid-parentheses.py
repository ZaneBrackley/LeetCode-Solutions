class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                open = stack.pop()
                if open == '(' and ch == ')' or open == '{' and ch == '}' or open == '[' and ch == ']':
                    continue
                else: return False
        if len(stack) == 0:
            return True
        return False
        