class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        def format_range(start, end):
            """
            :type start: int
            :type end: int
            :rtype: str
            """
            return str(nums[start]) if start == end else "{}->{}".format(nums[start], nums[end])

        if not nums:
            return []

        ranges = []
        n = len(nums)
        i = 0

        for j in range(1, n):
            if nums[j] != nums[j - 1] + 1:
                ranges.append(format_range(i, j - 1))
                i = j
        
        ranges.append(format_range(i, n - 1))

        return ranges
