class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        n = len(nums)
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                return True
            else:
                i += 1 
                j += 1
        return False