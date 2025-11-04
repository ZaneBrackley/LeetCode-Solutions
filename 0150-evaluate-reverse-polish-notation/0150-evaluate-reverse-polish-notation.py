class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        result = 0

        for i in range (len(tokens)):
            try:
                stack.append(int(tokens[i]))
            except ValueError:
                result = 0
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
        return stack[0]