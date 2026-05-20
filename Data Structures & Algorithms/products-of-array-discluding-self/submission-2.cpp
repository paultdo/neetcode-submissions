class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> new_nums(nums.size());
        vector<int> prefix(nums.size());
        vector<int> postfix(nums.size());

        // prefix product
        for(int i = 0; i < nums.size(); i++) {
            if(i == 0) {
                prefix[i] = nums[i];
            } else {
                prefix[i] = prefix[i - 1] * nums[i];
            }
        }

        //post fix product

        for(int i = nums.size() - 1; i >= 0; i--) {
            if(i == nums.size() - 1) {
                postfix[i] = nums[i];
            } else {
                postfix[i] = postfix[i + 1] * nums[i];
            }
        }

        for(int i = 0; i < nums.size(); i++) {
            if(i == 0) {
                new_nums[i] = 1 * postfix[i+1];
            } else if(i != nums.size() - 1) {
                new_nums[i] = prefix[i - 1] * postfix[i + 1];
            } else {
                new_nums[i] = prefix[i-1] * 1;
            }
        }



        return new_nums;
    }
};
