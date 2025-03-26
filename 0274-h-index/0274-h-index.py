class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        n = len(citations)
        idx = 0

        while idx < n and citations[idx] > idx:
            idx += 1
        return idx