class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> prev_nums;

        for(int i = 0; i < nums.size(); i++) {
            int other_num = target - nums.at(i);
            if(prev_nums.contains(other_num)) {
                if(prev_nums.at(other_num) < i) {
                    return {prev_nums.at(other_num), i};
                } else {
                    return {i, prev_nums.at(other_num)};
                }
            } else {
                prev_nums.insert({nums.at(i), i});
            }

        }

        return {-1, -1};
    }
};
