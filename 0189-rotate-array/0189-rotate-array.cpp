class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> nums2 = nums;
        k = k % nums.size();

        for(int i = 0; i < nums.size(); i++) {
            if(i < k) {
                nums[i] = nums2[nums.size()-k+i];
            } else {
                nums[i] = nums2[i-k];
            }
        }
    }
};
