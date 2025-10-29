class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = best = nums[0]
        for x in nums[1:]:
            curr = max(x, curr + x)
            best = max(best, curr)
        return best