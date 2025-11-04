class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(s) % 2 != 0:
            return False

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif len(stack) == 0:
                return False
            elif ch == ")" and stack.pop() == "(":
                continue
            elif ch == "}" and stack.pop() == "{":
                continue
            elif ch == "]" and stack.pop() == "[":
                continue
            else:
                return False
        if len(stack) != 0:
            return False
        return True