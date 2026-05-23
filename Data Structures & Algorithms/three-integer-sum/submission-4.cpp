class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        std::sort(nums.begin(), nums.end());

        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] > 0) {
                break;
            }
            if(i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int sum = nums.at(i) * -1;
            int p1 = i+1;
            int p2 = nums.size() - 1;

            while(p1 < p2) {

                int sum2 = nums.at(p1) + nums.at(p2);
                if(sum2 < sum) {
                    p1++;
                } else if(sum2 > sum) {
                    p2--;
                } else {
                    result.push_back({nums[p1], nums[p2], nums[i]});
                    p1++;
                    p2--;
                    while(p1 < p2 && nums.at(p1) == nums.at(p1-1)) {
                        p1++;
                    }
                }
            }
        }

        return result;
    }
};
