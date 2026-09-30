class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        stack = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in stack:
                stack[key] = []
            stack[key].append(word)
        return list(stack.values())
        