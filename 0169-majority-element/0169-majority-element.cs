public class Solution {
    public int MajorityElement(int[] nums) {
        int current = nums[0], count = 0;

        foreach (int num in nums) {
            if (count == 0) {
                current = num;
            }
            count += (num == current) ? 1 : -1;
        }

        return current;
    }
}