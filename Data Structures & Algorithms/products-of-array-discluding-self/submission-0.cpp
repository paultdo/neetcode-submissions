class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> new_nums(nums.size(), 1);
        for(int i = 0; i < nums.size(); i++) {
            for(int j = 0; j < nums.size(); j++) {
                if(i != j) {
                    new_nums[i] *= nums[j];
                }
            }
        }

        return new_nums;
    }
};
