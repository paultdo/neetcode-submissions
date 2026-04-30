#include <unordered_map>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> h_map;
        for(int i = 0; i < nums.size(); i++) {
            if(!h_map.contains(nums.at(i))) {
                h_map.insert({nums.at(i), 1});
            } else {
                return true;
            }
        }

        return false;
        
    }
};