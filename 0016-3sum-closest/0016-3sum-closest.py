class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        lowest = 2**31 - 1
        n = len(nums)

        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if curr == target:
                    return target
                elif abs(target - curr) < abs(target - lowest):
                    lowest = curr
                if curr > target:
                    right -= 1
                else:
                    left += 1

        return lowest
                
        