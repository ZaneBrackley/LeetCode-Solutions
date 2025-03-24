class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = maxReach = last = 0
      
        for i, val in enumerate(nums[:-1]):
            maxReach = max(maxReach, i + val)
          
            if last == i:
                jumps += 1
                last = maxReach
      
        return jumps