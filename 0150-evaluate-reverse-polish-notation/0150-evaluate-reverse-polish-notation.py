class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = {'+', '-', '*', '/'}
        result = 0

        for i in range (len(tokens)):
            if tokens[i] not in ops:
                stack.append(int(tokens[i]))
                continue
            val2 = stack.pop()
            val1 = stack.pop()
            if tokens[i] == '+':
                result = val1 + val2
            elif tokens[i] == '-':
                result = val1 - val2
            elif tokens[i] == '*':
                result = val1 * val2
            else:
                result = int(float(val1) / val2)
            stack.append(result)
            result = 0
        return stack[0]
